#Проверка ввода на положительное целое число
while True:
	try:
		x=int(input('Enter a number: '))
		if x<=0:
			print('A number must be bigger  than  zero!')
		else:
			break
	except ValueError:
		print ('Error! Not an integer number')

print ('You entered:', x)
max = 0
for i in str(x):
	if int(i)>max:
		max=int(i)
print ('The biggest digit in {0} is {1}'.format(x,max))



	
