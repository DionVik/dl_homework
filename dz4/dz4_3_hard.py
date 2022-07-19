#Программа создания файлов для списков слов начинающихся с одинаковой буквы
#читаем все слова из файла fruits в список main_lst
with open('fruits.txt', 'r', encoding = 'utf8') as f:
	main_lst = [line for line in f if line != '\n']
#создаём список первых букв
first_letter_lst =  list(map(chr, range(ord('А'), ord('Я')+1)))
print(first_letter_lst)

#для каждой буквы из списка первых букв ищем слова начинающиеся с этой буквы, помещаем их во временный список и записываем в файл
for i in first_letter_lst:
	lst_for_save = [] #список в котором будем хранить слова начинающиеся на i
	for j in main_lst:
		if j[0] == i:
			lst_for_save.append(j)
	if len(lst_for_save) != 0:
		file_name = 'fruits_'+i  #генерируем имя файла
		with open(file_name, 'w', encoding = 'utf8') as f:
			for k in lst_for_save:
				f.write(k)

			




