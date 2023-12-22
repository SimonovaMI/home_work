"""
Для проверки введенных данных и их форматирования.
"""

from datetime import date as d
import number_b.shopping_at_the_store.view.view as v


def check_format_product_attribute(category, product, cost, date):
    """Для проверки введенных данных при добавлении продукта в базу данных."""
    format_category = format_category_product(category)
    format_product = format_category_product(product)
    format_cost = check_format_cost(cost)
    format_date = check_format_date(date)
    if (format_category is not None and format_product is not None and format_cost is not None
            and format_date is not None):
        return format_category, format_product, format_cost, format_date


def format_category_product(atr):
    return str.capitalize(str.strip(atr))


def check_format_cost(cost):
    try:
        return float(cost)
    except ValueError:
        v.message('Cost is incorrect. Can be like this 9.99. Try again.')


def check_format_date(date):
    try:
        return d.fromisoformat(date)
    except ValueError:
        v.message('Date is incorrect. Can be like this 2018-12-01. Try again.')


def check_id(id_product):
    try:
        return int(id_product)
    except ValueError:
        v.message('Id is incorrect. Try again.')
