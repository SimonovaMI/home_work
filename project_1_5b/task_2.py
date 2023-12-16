"""Напишите функцию, которая принимает неограниченное количество
числовых аргументов и возвращает кортеж из двух списков: отрицательных
значений (отсортирован по убыванию); неотрицательных значений
(отсортирован по возрастанию)."""
import random as rn


def generate_numb():
    """Для генерации рандомного числа. Возвращает рандомное число."""
    return rn.randint(-100, 100)


def return_result(*args):
    """Для создания кортежа из списков с положительными числами и с отрицательными. Возвращает кортеж из списков."""
    positive_numb_list = list(filter(lambda x: x > 0, args))
    negative_numb_list = list(filter(lambda x: x < 0, args))
    result_tuple = (sorted(negative_numb_list, reverse=True), sorted(positive_numb_list))
    return result_tuple


def print_result():
    """Для вывода результата в консоль. Создание числовых аргументов для функции return_result.
    Вывод кортежа на печать."""
    # не поняла как сгенерировать разное количество аргументов
    print(return_result(generate_numb(), generate_numb(), generate_numb(), generate_numb(), generate_numb(),
                        generate_numb()))


print_result()
