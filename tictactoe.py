def print_board(symbols):
    print('---------')
    print('|', symbols[0], symbols[1], symbols[2], '|')
    print('|', symbols[3], symbols[4], symbols[5], '|')
    print('|', symbols[6], symbols[7], symbols[8], '|')
    print('---------')


def game_status(symbols):
    x_win = False
    o_win = False
    # check if impossible by count
    if (symbols.count('X') - 2 >= symbols.count('O')
            or symbols.count('O') - 2 >= symbols.count('X')):
        print('Impossible')
        return
    # idea to make better: make a nested  list of possibles and for each triple check if they are all equal
    # check if X wins
    if (symbols[0] == symbols[1] == symbols[2] == 'X'  # check rows
            or symbols[3] == symbols[4] == symbols[5] == 'X'
            or symbols[6] == symbols[7] == symbols[8] == 'X'
            or symbols[0] == symbols[3] == symbols[6] == 'X'  # check columns
            or symbols[1] == symbols[4] == symbols[7] == 'X'
            or symbols[2] == symbols[5] == symbols[8] == 'X'
            or symbols[0] == symbols[4] == symbols[8] == 'X'  # check diagonals
            or symbols[2] == symbols[4] == symbols[6] == 'X'):
        x_win = True
    # check if O wins
    if (symbols[0] == symbols[1] == symbols[2] == 'O'  # check rows
            or symbols[3] == symbols[4] == symbols[5] == 'O'
            or symbols[6] == symbols[7] == symbols[8] == 'O'
            or symbols[0] == symbols[3] == symbols[6] == 'O'  # check columns
            or symbols[1] == symbols[4] == symbols[7] == 'O'
            or symbols[2] == symbols[5] == symbols[8] == 'O'
            or symbols[0] == symbols[4] == symbols[8] == 'O'  # check diagonals
            or symbols[2] == symbols[4] == symbols[6] == 'O'):
        o_win = True
    # check if both X and O won (impossible)
    if x_win or o_win:
        if not o_win:
            print('X wins')
            return
        elif not x_win:
            print('O wins')
            return
        else:
            print('Impossible')
        return
    # check if game is finished (draw)
    if '_' not in symbols:
        print('Draw')
    # check if game is not finished
    else:
        print('Game not finished')
    return


def not_win(symbols):
    if (symbols[0] == symbols[1] == symbols[2] == 'X'  # check rows
            or symbols[3] == symbols[4] == symbols[5] == 'X'
            or symbols[6] == symbols[7] == symbols[8] == 'X'
            or symbols[0] == symbols[3] == symbols[6] == 'X'  # check columns
            or symbols[1] == symbols[4] == symbols[7] == 'X'
            or symbols[2] == symbols[5] == symbols[8] == 'X'
            or symbols[0] == symbols[4] == symbols[8] == 'X'  # check diagonals
            or symbols[2] == symbols[4] == symbols[6] == 'X'):
        print("X wins")
        return False
    if (symbols[0] == symbols[1] == symbols[2] == 'O'  # check rows
            or symbols[3] == symbols[4] == symbols[5] == 'O'
            or symbols[6] == symbols[7] == symbols[8] == 'O'
            or symbols[0] == symbols[3] == symbols[6] == 'O'  # check columns
            or symbols[1] == symbols[4] == symbols[7] == 'O'
            or symbols[2] == symbols[5] == symbols[8] == 'O'
            or symbols[0] == symbols[4] == symbols[8] == 'O'  # check diagonals
            or symbols[2] == symbols[4] == symbols[6] == 'O'):
        print("O wins")
        return False
    if ' ' not in symbols:
        print('Draw')
        return False
    return True


def valid_input(coordinate):
    if len(coordinate) != 2:
        print("You should enter numbers!")
        return False
    else:
        coord1, coord2 = coordinate
        if not coord1.isnumeric() or not coord2.isnumeric():
            print("You should enter numbers!")
            return False
        elif not 1 <= int(coord1) <= 3 or not 1 <= int(coord2) <= 3:
            print("Coordinates should be from 1 to 3!")
            return False
        else:
            return True


def not_occupied(x, y, symbols):
    # checks if the coordinates are in a space with a character not _
    if symbols[3 * (3 - y) + x - 1] != ' ':
        print("This cell is occupied! Choose another one!")
        return False
    else:
        return True


elements = "         "
print_board(elements)
# game_status(elements)

char_x = True
while not_win(elements):
    not_printed = True
    while not_printed:
        coordinates = input("Enter the coordinates: ").split()
        if valid_input(coordinates):
            x, y = int(coordinates[0]), int(coordinates[1])
            if not_occupied(x, y, elements):
                elements = list(elements)
                if char_x:
                    elements[3 * (3 - y) + x - 1] = 'X'
                    char_x = False
                else:
                    elements[3 * (3 - y) + x - 1] = 'O'
                    char_x = True
                print_board("".join(elements))
                not_printed = False
