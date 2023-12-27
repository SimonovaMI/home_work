"""
Model для создания, в случае ее отсутствия базы данных. Для реализации функций: ввода, удаления, чтения данных.
"""

import os.path
import pandas as pd
from datetime import date as d
from typing import Optional, Tuple

from shopping_at_the_store.model import filename


def create_db() -> None:
    df: pd.DataFrame = pd.DataFrame(columns=['Category', 'Product', 'Cost', 'Date'])
    df.to_csv(filename)


def check_db() -> bool:
    """Проверка наличия файла базы данных."""
    return os.path.isfile(filename)


def add_product(product_for_add: Tuple[str, str, float, d]) -> None:
    try:
        if check_db():
            df: pd.DataFrame = pd.read_csv(filename, usecols=['Category', 'Product', 'Cost', 'Date'])
            df.loc[len(df.index)] = product_for_add
            df.to_csv(filename)
        else:
            create_db()
            add_product(product_for_add)
    except IOError:
        raise IOError('Input/Output Error. Please try again.')


def read_all() -> Optional[pd.DataFrame]:
    try:
        df: pd.DataFrame = pd.read_csv(filename, usecols=['Category', 'Product', 'Cost', 'Date'])
        df['Date'] = pd.to_datetime(df.Date)
        return df
    except IOError:
        raise IOError('Input/Output Error. Check: db exist. Please try again.')


def delete_product(id_product: int) -> None:
    try:
        df: pd.DataFrame = pd.read_csv(filename, usecols=['Category', 'Product', 'Cost', 'Date']).drop([id_product])
        df.to_csv(filename)
    except KeyError:
        raise KeyError('Id is not found. Try again.')
    except IOError:
        raise IOError('Input/Output Error. Check: db exist. Please try again.')
