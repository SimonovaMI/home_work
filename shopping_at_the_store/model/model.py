"""
Model для создания, в случае ее отсутствия базы данных. Для реализации функций: ввода, удаления, чтения данных.
"""

import os.path
import pandas as pd

from number_b.shopping_at_the_store.model import filename


def create_db():
    df = pd.DataFrame(columns=['Category', 'Product', 'Cost', 'Date'])
    df.to_csv(filename)


def check_db():
    """Проверка наличия файла базы данных."""
    return os.path.isfile(filename)


def add_product(product_for_add):
    try:
        if check_db():
            df = pd.read_csv(filename, usecols=['Category', 'Product', 'Cost', 'Date'])
            df.loc[len(df.index)] = product_for_add
            df.to_csv(filename)
        else:
            create_db()
            add_product(product_for_add)
    except IOError:
        raise IOError('Input/Output Error. Please try again.')


def read_all():
    try:
        df = pd.read_csv(filename, usecols=['Category', 'Product', 'Cost', 'Date'])
        df['Date'] = pd.to_datetime(df.Date)
        return df
    except IOError:
        raise IOError('Input/Output Error. Check: db exist. Please try again.')


def delete_product(id_product):
    try:
        df = pd.read_csv(filename, usecols=['Category', 'Product', 'Cost', 'Date']).drop([id_product])
        df.to_csv(filename)
    except KeyError:
        raise KeyError('Id is not found. Try again.')
    except IOError:
        raise IOError('Input/Output Error. Check: db exist. Please try again.')
