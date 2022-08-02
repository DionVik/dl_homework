#Расчёт з.п. сотрудников в зависимости от отработанных часов
workers_lst = []
hours_lst = []
result_lst = []
#читаем файл workers.txt в список
with open ('workers.txt', 'r') as f:
	workers_lst = f.readlines()
#читаем файл hours.txt в список
with open('hours_of.txt', 'r') as f:
	hours_lst = f.readlines()
#удаляем из списков строки с шапкой таблицы
del(workers_lst[0])
del(hours_lst[0])

for i in workers_lst:
	wl = i.split()  #Элемент строку с данными работника преобразуем в список wl, в котором wl[0]=имя, wl[1] - фамилия
	for j in hours_lst:
		if (wl[0] in j) and (wl[1] in j): #если и имя и фамилия есть в строке из списка с отработанными часами
			hl = j.split()  #преобразуем эту строку в список hl, элемент hl[2], которого = количеству отработанных часов
			wl.append(hl[2]) #добавляем количество часов к списку с данными работника 
	result_lst. append(wl)  #добавляем полученный список в результирующий общий, элементы которого - списки данных работника 
	
for i in result_lst:
	oklad = float(i[2]) #оклад 
	norma = float(i[4]) #норма часов
	otrabotano = float(i[5]) #реально отработанное время
	oklad_v_chas = oklad / norma
	#если отработано меньше нормы, з.п. уменьшается пропорционально
	if otrabotano < norma:
		zp = oklad_v_chas * otrabotano
	elif otrabotano > norma: #если отработано больше нормы, з.п. каждый лишний час оплачивается по двойному тарифу
		pererabotka = otrabotano - norma
		zp = oklad + 2 * oklad_v_chas * pererabotka
	else:
		zp = oklad
	i.append(zp) #добавляем з.п. в список данных работника
#вывод результата	
shapka = ['Имя', 'Фамилия', 'Оклад', 'Должность', 'Норма', 'Отработано', 'Зарплата']			
print( '{0[0]:<10.15} {0[1]:<10.15} {0[2]:<10.15} {0[3]:<15} {0[4]:<10.15} {0[5]:<10.15} {0[6]:<10.15}'.format(shapka))
for i in result_lst:
	print( '{0[0]:<10.15} {0[1]:<10.15} {0[2]:<10.15} {0[3]:<15} {0[4]:<10.15} {0[5]:<10.15} {0[6]:<10.2f}'.format(i))
	 




	
	 
