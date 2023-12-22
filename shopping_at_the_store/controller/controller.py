"""
Controller для управления данными и интерфейсом программы.
"""

import number_b.shopping_at_the_store.view.view as v
import helper_for_check_format_product_attr as h_check_format
import number_b.shopping_at_the_store.model.DAO as DAO


def start_shopping():
    v.show_main_menu()
    choose_next_action()


def choose_next_action():
    while True:
        action = v.choose_action()
        if action is not None:
            break
    choose_action(action)


def choose_action(action):
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


def add_product():
    while True:
        category, product, cost, date = v.show_add_product_form()
        product_for_add = (
            h_check_format.check_format_product_attribute(category, product, cost, date)
        )
        if product_for_add is not None:
            break
    try:
        DAO.add_product(product_for_add)
        v.message('Product added!')
    except IOError as err:
        v.message(err)

    choose_next_action()


def show_all():
    try:
        v.show_result(DAO.show_all())

    except IOError as err:
        v.message(err)

    choose_next_action()


def show_for_param(param, param_item):
    try:
        v.show_result(DAO.show_filtered_data(param, param_item))
    except IOError as io_err:
        v.message(io_err)

    choose_next_action()


def show_by_min_max():
    try:
        v.show_result(DAO.show_by_min_max(True))
        v.show_result(DAO.show_by_min_max(False))
    except IOError as err:
        v.message(err)

    choose_next_action()


def delete_product():
    while True:
        id_product = v.show_delete_form()
        id_product = h_check_format.check_id(id_product)
        if id_product is not None:
            break
    try:
        DAO.delete_product(id_product)
        v.message('Product deleted!')
    except Exception as err:
        v.message(err)

    choose_next_action()


def choose_filter_param(menu_item):
    try:
        if menu_item == 3:
            set_params = map(lambda date: date.strftime('%Y-%m-%d'), DAO.show_unique_value('Date'))
            param_item = v.show_filter_form('date', set_params)
            if h_check_format.check_format_date(param_item):
                show_for_param('Date', param_item)

        elif menu_item == 4:
            param_item = v.show_filter_form('category', DAO.show_unique_value('Category'))
            show_for_param('Category', h_check_format.format_category_product(param_item))
    except TypeError as t_err:
        v.message('DB is empty. Try add product.')

    choose_next_action()


start_shopping()
