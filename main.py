import random

field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def display_field():
    print('\n', field[0], '\n', field[1], '\n', field[2])


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
        col = int(input('Колонка - '))-1
        row = int(input('Ряд - '))-1
        while field[row][col].strip():
            print('ВЫБРАННАЯ КЛЕТКА ЗАНЯТА!')
            col = int(input('Колонка - ')) - 1
            row = int(input('Ряд - ')) - 1
        field[row][col] = 'X'
        last_went = 2
        print('Вы походили')
        display_field()
    else:
        rand_col = random.choice([0, 1, 2])
        rand_row = random.choice([0, 1, 2])
        while field[rand_row][rand_col].strip():
            rand_col = random.choice([0, 1, 2])
            rand_row = random.choice([0, 1, 2])
        field[rand_row][rand_col] = 'O'
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
