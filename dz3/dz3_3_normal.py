import random
lst = []
n=int(input ('Задайте количество чисел: '))
for i in range(n):
	k = random.randint(-100, 100)
	lst.append(k)
print ('Список целых чисел от -100 до 100: {}'.format(lst))


