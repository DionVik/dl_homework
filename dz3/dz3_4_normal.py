lst = [1,2,3,5,2,1,8]

lst2=list(set(lst))  #список из которого исключены повторения
lst3=[] #список содержащий только неповторяющиеся элементы из списка lst
for i in lst:
	if lst.count(i) == 1:
		lst3.append(i)	
print ('Исходный список: {}'.format(lst))
print('Список, из которого исключены повторения: {}'.format(lst2))
print('Список, состоящий из неповторяющихся элементов исходного списка: {}'.format(lst3))





