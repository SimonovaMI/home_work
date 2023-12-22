"""
View для реализации взаимодействия с пользователем. Формы ввода/вывода.
"""

import pandas as pn


def show_main_menu():
    print(f'''Hello 
         1.Add
         2.Show all
         3.Show for date
         4.Show by category
         5.Show by min->max, max->min cost
         6.Delete
         0.Exit''')


def choose_action():
    """Выбор действия из главного меню."""
    try:
        action = int(input('What would you like to do? '))
        if action not in (0, 1, 2, 3, 4, 5, 6):
            raise ValueError('Value is incorrect')
        return action
    except ValueError:
        print('Value is incorrect. Try again.')


def show_add_product_form():
    category = input('Category: ')
    product = input('Product: ')
    cost = input('Cost: ')
    date = input('Date: ')
    return category, product, cost, date


def show_exit_form():
    print('Thanks!Have a good day!')


def show_result(result):
    """Вывод результата манипуляций с базой данных."""
    if not pn.DataFrame(result).empty:
        print(result)
    else:
        print('No data')


def message(text):
    print(text)


def show_delete_form():
    id_product = input('Input id product. ')
    return id_product


def show_filter_form(param_title, set_params):
    print('Choose ' + param_title)
    if not pn.DataFrame(set_params).empty:
        print(*set_params, sep='\n')
        param_item = input(param_title + ': ')
        return param_item
    else:
        print('No data')
