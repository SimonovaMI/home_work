"""
View для реализации взаимодействия с пользователем. Формы ввода/вывода.
"""

import pandas as pd  # type: ignore
from typing import Optional, List


def show_main_menu() -> None:
    print(f'''Hello 
         1.Add
         2.Show all
         3.Show for date
         4.Show by category
         5.Show by min->max, max->min cost
         6.Delete
         0.Exit''')


def choose_action() -> Optional[int]:
    """Выбор действия из главного меню."""
    try:
        action: int = int(input('What would you like to do? '))
        if action not in (0, 1, 2, 3, 4, 5, 6):
            raise ValueError('Value is incorrect')
        return action
    except ValueError:
        print('Value is incorrect. Try again.')


def show_add_product_form() -> (str, str, str, str):
    category: str = input('Category: ')
    product: str = input('Product: ')
    cost: str = input('Cost: ')
    date: str = input('Date: ')
    return category, product, cost, date


def show_exit_form() -> None:
    print('Thanks!Have a good day!')


def show_result(result: pd.DataFrame) -> None:
    """Вывод результата манипуляций с базой данных."""
    if not pd.DataFrame(result).empty:
        print(result)
    else:
        print('No data')


def message(text: str) -> None:
    print(text)


def show_delete_form() -> str:
    id_product: str = input('Input id product. ')
    return id_product


def show_filter_form(param_title: str, set_params: List[str]) -> Optional[str]:
    print('Choose ' + param_title)
    if not pd.DataFrame(set_params).empty:
        print(*set_params, sep='\n')
        param_item: str = input(param_title + ': ')
        return param_item
    else:
        print('No data')
