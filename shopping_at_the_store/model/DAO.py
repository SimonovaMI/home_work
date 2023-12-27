"""
DAO для взаимодействия с базой данных. Для реализации возможности манипуляций с данными.
"""

import pandas as pd
from datetime import date as d
from typing import Tuple, List
import shopping_at_the_store.model.model as m


def add_product(product_for_add: Tuple[str, str, float, d]) -> None:
    m.add_product(product_for_add)


def show_all() -> pd.DataFrame:
    return m.read_all()


def show_filtered_data(column: str, arg: str) -> pd.DataFrame:
    """Для создания data frame для отфильтрованных данных по заданному параметру."""
    df = m.read_all()
    filtered_df: pd.DataFrame = df[df[column] == arg]
    return filtered_df


def show_by_min_max(ascending: bool) -> pd.DataFrame:
    """Для создания data frame с сортировкой от минимальной к максимальной стоимости и от максимальной к минимальной."""
    df: pd.DataFrame = m.read_all().sort_values(by='Cost', ascending=ascending)
    return df


def delete_product(id_product: int):
    m.delete_product(id_product)


def show_unique_value(param_tittle: str) -> List[str]:
    """Для создания списка выбора возможных вариантов для фильтрации данных."""
    df: pd.DataFrame = m.read_all()
    df: pd.DataFrame = df[param_tittle].unique()
    return df.tolist()
