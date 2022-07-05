name=input('Введите ваше имя: ')
age=input('Введите ваш возраст: ')
raznica = int(age) - 18
second_digit = raznica %10
if second_digit ==1:
	print(name+' на '+str(raznica)+' год больше 18.')
elif second_digit in (2,3,4):
	print(name+' на '+str(raznica)+' года больше 18.')
else:	
	print(name + ' на '+ str(raznica)+' лет больше 18.')


