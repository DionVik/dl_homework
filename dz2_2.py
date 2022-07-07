x = None  
while x==None:
	x=input("Введите:'чётные' или 'нечётные': ") 
	print ('Вы ввели: ', x)
	if (x != 'чётные') and (x != 'нечётные'):
		print('Я не понимаю, что вы от меня хотите!')
		x=None
	else:
		break
if x == 'чётные':
	for i in range(21):
		if i%2 == 0:
			print(i, end=' ')
else:
	for i in range(21):
		if i%2 != 0:
			print(i, end=' ')
print()


		
		
