"""Задание: дан список температурных изменений в течение дня (целые числа). Известно,
что измеряющее устройство иногда сбоит и записывает отсутствие
температуры (значение None). Выведите среднюю температуру за
наблюдаемый промежуток времени, предварительно очистив список от
неопределенных значений. Гарантируется, что хотя бы одно определенное
значение в списке есть."""

import random as rn
import statistics as stat


def generate_temp_list():
    """Имитация списка измерений. Возвращает список из 10 рандомных значений, среди которых рандомное
    число раз может встречаться значение None."""
    measurements_count = 10
    random_temp_list = [rn.randint(-40, 40) for i in range(measurements_count)]
    none_count = rn.randint(0, measurements_count - 2)
    while none_count != 0:
        random_temp_list[rn.randint(0, measurements_count - 1)] = None
        none_count -= 1

    return random_temp_list


def calculate_the_average_temp():
    """Возвращает среднее значения температур"""
    average_temp = stat.mean(list(filter(lambda x: isinstance(x, int), generate_temp_list())))
    return average_temp


def print_result():
    """Вывод результатов"""
    print(f'''{calculate_the_average_temp():0.2f}''')


print_result()
