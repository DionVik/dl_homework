import math
list1= [23,16,81,4,144]
print('Исходный список: {}'.format(list1))
new_list = []
for i in list1:
	try:
		k=math.sqrt(i)
		if k*10%10 != 0:  #если имеется десятичная часть - пропускаем
			continue
		else:
			k=int(k)	
			new_list.append(k)  
	except ValueError:     #если возникает исключение - пропускаем элемент
		continue
print ('Cписок из квадратных корней элементов исходного списка: {}'.format(new_list))		
