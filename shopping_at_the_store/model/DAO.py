"""
DAO для взаимодействия с базой данных. Для реализации возможности манипуляций с данными.
"""

import number_b.shopping_at_the_store.model.model as m


def add_product(product_for_add):
    m.add_product(product_for_add)


def show_all():
    return m.read_all()


def show_filtered_data(column, arg):
    """Для создания data frame для отфильтрованных данных по заданному параметру."""
    df = m.read_all()
    filtered_df = df[df[column] == arg]
    return filtered_df


def show_by_min_max(ascending):
    """Для создания data frame с сортировкой от минимальной к максимальной стоимости и от максимальной к минимальной."""
    df = m.read_all().sort_values(by='Cost', ascending=ascending)
    return df


def delete_product(id_product):
    m.delete_product(id_product)


def show_unique_value(param_tittle):
    """Для создания списка выбора возможных вариантов для фильтрации данных."""
    df = m.read_all()
    df = df[param_tittle].unique()
    return df.tolist()
