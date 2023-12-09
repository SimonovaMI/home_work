input_list = []
while True:
    word = str(input('Введите слово:'))
    if word == '':
        break
    input_list.append(word)

print(''.join([str(i)[0] for i in input_list]))
