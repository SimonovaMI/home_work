"""
Controller для управления данными и интерфейсом программы.
"""

from typing import Tuple, Optional
from datetime import date as d
import shopping_at_the_store.view.view as v
import helper_for_check_format_product_attr as h_check_format
import shopping_at_the_store.model.DAO as DAO


def start_shopping() -> None:
    v.show_main_menu()
    choose_next_action()


def choose_next_action() -> None:
    while True:
        action: Optional[int] = v.choose_action()
        if action is not None:
            break
    choose_action(action)


def choose_action(action: int) -> None:
    match action:
        case 0:
            v.show_exit_form()
        case 1:
            add_product()
        case 2:
            show_all()
        case 3:
            choose_filter_param(3)
        case 4:
            choose_filter_param(4)
        case 5:
            show_by_min_max()
        case 6:
            delete_product()


def add_product() -> None:
    while True:
        category, product, cost, date = v.show_add_product_form()
        product_for_add: Tuple[str, str, float, d] = (
            h_check_format.check_format_product_attribute(category, product, cost, date)
        )
        if product_for_add is not None:
            break
    try:
        DAO.add_product(product_for_add)
        v.message('Product added!')
    except IOError as err:
        v.message(str(err))

    choose_next_action()


def show_all() -> None:
    try:
        v.show_result(DAO.show_all())
    except IOError as err:
        v.message(str(err))

    choose_next_action()


def show_for_param(param: str, param_item: str) -> None:
    try:
        v.show_result(DAO.show_filtered_data(param, param_item))
    except IOError as io_err:
        v.message(str(io_err))

    choose_next_action()


def show_by_min_max() -> None:
    try:
        v.show_result(DAO.show_by_min_max(True))
        v.show_result(DAO.show_by_min_max(False))
    except IOError as err:
        v.message(str(err))

    choose_next_action()


def delete_product() -> None:
    while True:
        id_product: str = v.show_delete_form()
        id_product: int = h_check_format.check_id(id_product)
        if id_product is not None:
            break
    try:
        DAO.delete_product(id_product)
        v.message('Product deleted!')
    except Exception as err:
        v.message(str(err))

    choose_next_action()


def choose_filter_param(menu_item: int) -> None:
    try:
        if menu_item == 3:
            set_params: map = map(lambda date: date.strftime('%Y-%m-%d'), DAO.show_unique_value('Date'))
            param_item: str = v.show_filter_form('date', list(set_params))
            if h_check_format.check_format_date(param_item):
                show_for_param('Date', param_item)

        elif menu_item == 4:
            param_item: str = v.show_filter_form('category', DAO.show_unique_value('Category'))
            show_for_param('Category', h_check_format.format_category_product(param_item))
    except TypeError:
        v.message('DB is empty. Try add product.')

    choose_next_action()


start_shopping()
