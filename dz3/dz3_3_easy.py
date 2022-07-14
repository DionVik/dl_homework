list1 = [1,2,3,4,5]
print ('Дан список: {}'.format(list1))
new_list = []
for i in list1:
	if i%2==0:
		k=i/4
	else:
		k=i*2
	new_list.append(k)
print('Элементы кратные 2 делим на 4, элементы не кратные 2 - умножаем на 2')
print ('Получен новый список {}'.format(new_list))

