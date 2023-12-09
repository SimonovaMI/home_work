import random as rn

random_threshold = rn.randint(1, 100)


def check(number, threshold=random_threshold):
    if int(number) > int(threshold):
        return 'High'
    elif int(number) < int(threshold):
        return 'Low'
    else:
        return 'Equals'


random_numbers_list = [rn.randint(1, 100) for i in range(100)]
result_list = map(check, random_numbers_list)

print(list(result_list))
