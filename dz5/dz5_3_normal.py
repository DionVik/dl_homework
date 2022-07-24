# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import re

file_name= 'digits.txt'   #имя файла
#записываем в файл 2500 символов случайных цифр 
with open(file_name, 'w', encoding='utf8') as f:
	for i in range(2500):
		f.write(str(random.randint(0,9)))
#читаем из файла строку цифр в source		
with open(file_name, 'r', encoding='utf8') as f:
	source = f.read()
	
#получаем список последовательностей цифр с количеством больше 2:
strings=re.findall(r'0{2,}|1{2,}|2{2,}|3{2,}|4{2,}|5{2,}|6{2,}|7{2,}\
|8{2,}|9{2,}', source) 

max_length=0 #наибольшая длина последовательности
max_string_list=[] #массив наибольших последовательностей
for i in strings:
	if len(i) > max_length:
		max_length = len(i)
		
for i in strings:
	if len(i)==max_length:
		max_string_list.append(i)
	
print('Из последовательностей цифр {} наибольшими являются {}'.format(strings, max_string_list))

	



