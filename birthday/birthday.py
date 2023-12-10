def print_date(input_date):
    print(f'''{input_date[1]}.{input_date[0]}''')


while True:
    input_month = int(input('Введите месяц Вашего рождения: '))
    input_day = int(input('Введите число месяца, когда Вы родились: '))
    match [input_month, input_day]:
        case[input_month, input_day] if 1 <= input_day <= 31 and input_month in (1, 3, 5, 7, 8):
            print_date(['0' + str(input_month), input_day])
            break
        case [2, input_day] if 1 <= input_day <= 29:
            print_date(['02', input_day])
            break
        case [input_month, input_day] if 1 <= input_day <= 31 and input_month in (10, 12):
            print_date([input_month, input_day])
            break
        case [input_month, input_day] if 1 <= input_day <= 30 and input_month in (4, 6, 9):
            print_date(['0' + str(input_month), input_day])
            break
        case [11, input_day] if 1 <= input_day <= 30:
            print_date([11, input_day])
            break
        case _:
            print('Неверная дата')
