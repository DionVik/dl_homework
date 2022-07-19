#функция сортирующая список по возрастанию
def sort_to_max(lst):
	for i in range(0, (len(lst)-1)):
		for j in range(0, (len(lst)-1)):
			if lst[j] > lst[j+1]:
				lst[j],lst[j+1] = lst[j+1],lst[j]
	return lst
	
	
lst = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print('Оригинальный список: ',lst)
print('Отсортированный список: ',sort_to_max(lst))
