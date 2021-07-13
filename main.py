# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def game():
    print("""
    Добро пожаловать в игру «Крестики-нолики».
    Для игры нужно два игрока.
    Введите кординаты в формате, например 11.
    ------------------------------------------
    """)

    gamer_one = input("Игрок 1(Введите Имя): ")
    gamer_two = input("Игрок 2(Введите Имя): ")

    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"],
    ]

    __show_board(board)
    __gamer_actions_handler(board, gamer_one, gamer_two)


def __gamer_actions_handler(board, gamer_one, gamer_two):
    step = 0
    while True:
        gamer_name = gamer_one if step % 2 == 0 else gamer_two
        action = input("Ход игрока (%s): " % gamer_name)
        try:
            coordinate_x, coordinate_y = map(int, list(action))
            print(coordinate_x, coordinate_y, (coordinate_x not in range(0, 3) and coordinate_y not in range(0, 3)) and board[coordinate_x][coordinate_y] != "_")
            if (coordinate_x not in range(0, 3) or coordinate_y not in range(0, 3)) or board[coordinate_x][coordinate_y] != "_":
                raise ValueError
        except ValueError:
            __show_board(board)
            print("Некоректные кординаты: введите коректные кординаты в формате %s%s")
            continue

        board[coordinate_x][coordinate_y] = 'X' if step % 2 == 0 else '0'

        step += 1
        __show_board(board)
        result = __check_if_winner_exist(board)
        if result == "X":
            print("Победитель - %s" % gamer_one)
            break
        elif result == "0":
            print("Победитель - %s" % gamer_two)
            break
        elif result:
            print("Ничья!!!")
            break


def __check_if_winner_exist(board):
    def check_set(board_coordinate_value_list):
        coordinate_value_set = list(set(board_coordinate_value_list))
        if len(coordinate_value_set) == 1 and coordinate_value_set[0] != "_":
            return coordinate_value_set[0]

    for row in board:
        result = check_set(row)
        if result is not None:
            return result

    for column in range(3):
        result = check_set([colVal[column] for colVal in board])
        if result is not None:
            return result

    c1 = check_set([board[0][0], board[1][1], board[2][2]])
    c2 = check_set([board[0][2], board[1][1], board[2][0]])

    if c1 is not None:
        return c1
    if c2 is not None:
        return c2

    is_all_coordinates_filled = True
    for row in board:
        if "_" in row:
            is_all_coordinates_filled = False
            break

    return is_all_coordinates_filled


def __show_board(board):
    print("Доска игры:")
    print(" ", 0, 1, 2)
    for item in enumerate(board):
        print(item[0], *item[1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
