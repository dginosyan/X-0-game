# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def game():
    gamer_one = input("Игрок 1(Введите Имя): ")
    gamer_two = input("Игрок 2(Введите Имя): ")

    board = [
        ["_","_","_"],
        ["_","_","_"],
        ["_","_","_"],
    ]

    showBoard(board)

    step = 0
    while True:
        if step % 2 == 0:
            action = input("Ход игрока 1(%s): " % gamer_one)
            x, y = map(int, list(action))
            if (x in range(0,3) and y in range(0,3)) and board[x][y] == "_":
                board[x][y] = 'X'
            else:
                showBoard(board)
                print("Wrong cordinates: try it again")
                continue
        else:
            action = input("Ход игрока 2(%s): " % gamer_two)
            x, y = map(int, list(action))
            if (x in range(0,3) and y in range(0,3)) and board[x][y] == "_":
                board[x][y] = '0'
            else:
                showBoard(board)
                print("Wrong cordinates: try it again")
                continue
        step += 1
        showBoard(board)
        result = checkIfWinnerExist(board)
        if result == "X":
            print("Winner is %s" % gamer_one)
            break
        elif result == "0":
            print("Winner is %s" % gamer_two)
            break
        elif result is False:
            break


def checkIfWinnerExist(board):
    def checkSet(l):
        if len(l) == 1 and l[0] != "_":
            return l[0]
    for row in board:
        result = checkSet(list(set(row)))
        if result is not None:
            return result

    for column in range(3):
        colSet = list(set([colVal[column] for colVal in board]))
        result = checkSet(colSet)
        if result is not None:
            return result

    c1 = checkSet(list(set([board[0][0], board[1][1], board[2][2]])))
    c2 = checkSet(list(set([board[0][2], board[1][1], board[2][0]])))
    # print(c1, c2, [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]], "C1C2")

    if c1 is not None:
        return c1
    if c2 is not None:
        return c2

    status = True
    for row in board:
        if "_" in row:
            status = False
            break

    if status:
        print("Nichia")
        return False




def showBoard(board):
    print("Board:")
    print(" ", 0, 1, 2)

    for item in enumerate(board):
        print(item[0], *item[1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
