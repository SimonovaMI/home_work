from random import randint


n_comp = randint(1, 100)
print(n_comp)
print('Компьютер "загадал" число в интервале от 1 до 100. Какое?')


def count_attempts(func):
    def wrapper(arg1, arg2):
        wrapper.n = getattr(wrapper, 'n', 0) + 1
        return func(arg1, arg2, wrapper.n)
    return wrapper


@count_attempts
def check_numder(numder, n_comp, n):
    if numder > n_comp:
        return 'Загаданное число меньше'
    elif otvet < n_comp:
        return 'Загаданное число больше.'
    else:
        return f'Правильно! Число попыток отгадывания - {n}'


while True:
    otvet = int(input('Введите Ваше число '))
    answer = check_numder(otvet, n_comp)
    print(answer)
    if otvet == n_comp:
        break
