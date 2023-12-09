def print_date(input_date):
    print(f'''{input_date[1]}.{input_date[0]}''')


while True:
    input_month = int(input('Введите месяц Вашего рождения: '))
    input_day = int(input('Введите число месяца, когда Вы родились: '))
    match [input_month, input_day]:
        case [1, input_day] if 1 <= input_day <= 31:
            print_date(['01', input_day])
            break
        case [2, input_day] if 1 <= input_day <= 29:
            print_date(['02', input_day])
            break
        case [3, input_day] if 1 <= input_day <= 31:
            print_date(['03', input_day])
            break
        case [4, input_day] if 1 <= input_day <= 30:
            print_date(['04', input_day])
            break
        case [5, input_day] if 1 <= input_day <= 31:
            print_date(['05', input_day])
            break
        case [6, input_day] if 1 <= input_day <= 30:
            print_date(['06', input_day])
            break
        case [7, input_day] if 1 <= input_day <= 31:
            print_date(['07', input_day])
            break
        case [8, input_day] if 1 <= input_day <= 31:
            print_date(['08', input_day])
            break
        case [9, input_day] if 1 <= input_day <= 30:
            print_date(['09', input_day])
            break
        case [10, input_day] if 1 <= input_day <= 31:
            print_date([10, input_day])
            break
        case [11, input_day] if 1 <= input_day <= 30:
            print_date([11, input_day])
            break
        case [12, input_day] if 1 <= input_day <= 31:
            print_date([12, input_day])
            break
        case _:
            print('Неверная дата')
