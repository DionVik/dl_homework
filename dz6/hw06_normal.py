# Задача-1:
# Примечание: Если уже делали easy задание, то просто перенесите решение сюда.
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))

#Решение:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).
	
    Результат:
        - float.
    """
    return (a * b) ** 0.5

try:
	a = float(input("a = "))
	b = float(input("b = "))
	c = avg(a, b)
	print("Среднее геометрическое = {:.2f}".format(c))
except (ValueError, TypeError) as error:
	print(error)


# ПРИМЕЧАНИЕ: Для решения задачи 2-3 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
	
menu ="""
Выберите действие (Выбор: '1'-'4' Выход: 'q'):
1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку 
"""

while True:
	print(menu)
	i = input()
	if i in ('1', '2', '3', '4', 'q'):
		if i == '1':
			try:
				path_to_folder = input('Введите путь к папке: ')
				os.chdir(path_to_folder)
			except FileNotFoundError:
				print('Невозможно перейти')
			else:
				print('Успешно перешёл')	
		elif i == '2':
			for root, dirs, files in os.walk(os.getcwd()):
				for directory in dirs:
					print(directory)
				for item in files:
					print(item)
		elif i == '3':
			try:
				path_to_folder = input('Введите путь к папке, которую хотите удалить: ')
				os.rmdir(path_to_folder)	
			except FileNotFoundError:
				print('Невозможно удалить')
			except PermissionError:
				print('Невозможно удалить')
			except OSError:
				print('Невозможно удалить')
			else:
				print('Успешно удалена')
		elif i == '4':
			try:
				path_to_folder = input('Введите путь к папке, которую хотите создать: ')
				os.mkdir(path_to_folder)
			except FileExistsError:
				print('Невозможно создать')
			except PermissionError:
				print('Невозможно создать')	
			else:
				print('Успешно созадана')	
		elif i == 'q':
			break
sys.exit()
