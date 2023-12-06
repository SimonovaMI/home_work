ticket_number = input('Введите номер билета: ')

ticket_number_tuple = tuple(ticket_number.strip(' '))
summ_first_part = 0
summ_last_part = 0
for i in range(len(ticket_number_tuple)):
    if i < 3:
        summ_first_part += int(ticket_number_tuple[i])
    else:
        summ_last_part += int(ticket_number_tuple[i])

if summ_last_part == summ_first_part:
    print('Билет счастливый')
else:
    print('Билет несчастливый')

