def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    for i in (ticket_number[:3]):
        sum1=sum1+int(i)
    for j in (ticket_number[3:]):
        sum2 = sum2+int(j)   
    if sum1 == sum2:
        return True
    else:
        return False


number = input('Введите 6 значный номер билета: ')
if lucky_ticket(number):
    print('Билет счастливый')
else:
    print('Билет несчастливый')
