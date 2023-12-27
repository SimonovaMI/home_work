"""
Для проверки введенных данных и их форматирования.
"""

from typing import Optional
from datetime import date as d
import shopping_at_the_store.view.view as v


def check_format_product_attribute(category: str, product: str, cost: str, date: str) -> (str, str, float, d):
    """Для проверки введенных данных при добавлении продукта в базу данных."""
    format_category: str = format_category_product(category)
    format_product: str = format_category_product(product)
    format_cost: float = check_format_cost(cost)
    format_date: d = check_format_date(date)
    if (format_category is not None and format_product is not None and format_cost is not None
            and format_date is not None):
        return format_category, format_product, format_cost, format_date


def format_category_product(atr: str) -> str:
    return str.capitalize(str.strip(atr))


def check_format_cost(cost: str) -> Optional[float]:
    try:
        return float(cost)
    except ValueError:
        v.message('Cost is incorrect. Can be like this 9.99. Try again.')


def check_format_date(date: str) -> Optional[d]:
    try:
        return d.fromisoformat(date)
    except ValueError:
        v.message('Date is incorrect. Can be like this 2018-12-01. Try again.')


def check_id(id_product: str) -> Optional[int]:
    try:
        return int(id_product)
    except ValueError:
        v.message('Id is incorrect. Try again.')
