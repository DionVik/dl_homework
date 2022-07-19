#реализация функции filter
#применяет функцию к элементам последовательности и возвращает последовательность из элементов,
# для которых функция возвратит True
def my_filter(funk, lst):
	result=[]
	for i in lst:
		if funk(i):
			result.append(i)
	return result
		
spisok = [1,2,3,4,5]
#функция проверки чётности числа для примера
def proverka_chetnosti(el):
	if el%2==0:
		return True
	else:
		return False		

a= my_filter(proverka_chetnosti, spisok)

print('Для списка {} и функции проверки чётности применим функцию my_filter'.format(spisok))
print ('Результат: {}'.format(a))


 
