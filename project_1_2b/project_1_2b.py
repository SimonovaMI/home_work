product_list = ['product' + str(i) for i in range(1, 11)]
price_list = [i for i in range(1, 11)]
employee_list = ['00' + str(i) for i in range(1, 10)]
employee_list.append('010')

result_list = []
for i, j, k in zip(product_list, price_list, employee_list):
    result_list.append((i, j, k))

print(result_list)
