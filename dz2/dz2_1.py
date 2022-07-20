#функция проверки ввода пользователя - в параметрах - сообщение о вводе, допустимость нуля, допустимость минуса
def get_int(msg, zero_allowed, minus_allowed):
	while True:
		try:
			x = int(input(msg))
			if zero_allowed == False and x == 0:    #ноль запрещён
				print('Вы ввели неверное значение. Введите положительное целое число больше 0.')
				continue
			elif minus_allowed == False and x < 0:  #минус запрещён
				print('Вы ввели неверное значение. Введите положительное целое число больше 0.')
				continue
			else:
				return x
		except ValueError: #исключение, если передано некорректное значение
			print('Вы ввели неверное значение. Введите положительное целое число больше 0.')


age = get_int ('Введите ваш возраст: ', False, False)
if age >= 18:
	print('Доступ разрешён')
else:
	print('Извините, пользоваться данным ресурсом можно только с 18 лет')