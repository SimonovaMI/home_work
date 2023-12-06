first_last_name = input('Введите имя и фамилию по форме: "имя фамилия" :')

first_name, last_name = tuple(first_last_name.strip(' ').split(' '))
first_name = first_name.capitalize()
last_name = last_name.capitalize()
login = last_name[0:4] + first_name[0]

print(f'''{last_name} {first_name}: {login}''')
