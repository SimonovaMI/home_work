"""Составьте две функции для возведения числа в степень: один из вариантов
реализуйте в рекурсивном стиле."""

import random as rn


def generate_number():
    """Возвраащет число."""
    return rn.randint(0, 10)


def generate_pow():
    """Возвращает степень числа."""
    return rn.randint(0, 10)


def pow_number(number, p):
    """Возведение в степень."""
    return number ** p


def rec_pow_number(number, p):
    """Рекурсивное возведение в степень."""
    if p == 0:
        return 1
    return number * rec_pow_number(number, p - 1)


def print_result():
    """Вывод результата."""
    number = generate_number()
    p = generate_pow()
    print(pow_number(number, p))
    print(rec_pow_number(number, p))


print_result()
