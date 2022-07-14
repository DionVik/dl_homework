def proverka(date):
	if len(date) != 10:  #проверка на длину
		return False
	if date[2] != '.' or date[5] !='.':  #проверка на разделители
		return False

	#выделяем день, месяц и год из строки
	year = int(date[6:])
	month = int(date[3:5])
	day = int(date[:2])
	
	#проверяем диапазоны чисел
	if year >=1 and year <= 9999:
		if month >=1 and month <= 12:
			if day>=1 and day <=31  and month in (1,3,5,7,8,10,12):
				return True
			if day>=1 and day <=30 and month in (2, 4, 6, 9, 11):
				return True
		else:
			return False

date = input ('Введите дату в формате дд.мм.гггг: ')
if proverka(date):
	print('Ввод верный')
else:
	print('Ввод неверный')


