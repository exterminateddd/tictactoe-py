import random

field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def display_field():
    print('\n', field[0], '\n', field[1], '\n', field[2])


def get_col_arr(col):
    return [field[0][col], field[1][col], field[2][col]]


def choose_pos():
    # rand_col_ = random.choice([0, 1, 2])
    # rand_row_ = random.choice([0, 1, 2])
    # while field[rand_row_][rand_col_].strip():
    #     rand_col_ = random.choice([0, 1, 2])
    #     rand_row_ = random.choice([0, 1, 2])
    many_occurs_cols = [0]
    many_occurs_rows = [0]
    for i in range(len(field)):
        if field[i].count('X') >= 2:
            many_occurs_rows.append(i)
    for i in range(len([get_col_arr(0), get_col_arr(1), get_col_arr(2)])):
        if field[i].count('X') >= 2:
            many_occurs_cols.append(i)
    pos_col = random.choice(many_occurs_cols)
    pos_row = random.choice(many_occurs_rows)
    while field[pos_row][pos_col].strip():
        pos_col = random.choice([0, 1, 2])
        pos_row = random.choice([0, 1, 2])
    return [pos_col, pos_row]


def check_win_bot():
    if field[0][0] == field[1][0] == field[2][0] == 'O':
        return True
    if field[0][1] == field[1][1] == field[2][1] == 'O':
        return True
    if field[0][2] == field[1][2] == field[2][2] == 'O':
        return True
    for r in field:
        if r.count('O') == 3 or r.count('X') == 3:
            if r.count('O') == 3:
                return True
    if field[0][0] == field[1][1] == field[2][2] == 'O' or field[0][2] == field[1][1] == field[2][0] == 'O':
        return True


def check_win_pl():
    if field[0][0] == field[1][0] == field[2][0] == 'X':
        return True
    if field[0][1] == field[1][1] == field[2][1] == 'X':
        return True
    if field[0][2] == field[1][2] == field[2][2] == 'X':
        return True
    for r in field:
        if r.count('X') == 3:
            if r.count('X') == 3:
                return True
    if field[0][0] == field[1][1] == field[2][2] == 'X' or field[0][2] == field[1][1] == field[2][0] == 'X':
        return True


display_field()


last_went = 1

while True:
    if last_went == 1:
        col = int(input('Колонка - ')) - 1
        row = int(input('Ряд - ')) - 1
        while field[row][col].strip():
            print('ВЫБРАННАЯ КЛЕТКА ЗАНЯТА!\nВведите новые координаты:')
            col = int(input('Колонка - ')) - 1
            row = int(input('Ряд - ')) - 1
        field[row][col] = 'X'
        last_went = 2
        print('Вы походили')
        display_field()
    else:
        chosen_pos = choose_pos()
        field[chosen_pos[1]][chosen_pos[0]] = 'O'
        print('Соперник походил')
        display_field()
        last_went = 1
    if check_win_bot():
        print('============')
        print('BOT WON')
        exit()
    if check_win_pl():
        print('============')
        print('YOU WON')
        exit()
