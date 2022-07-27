# Задача-1:
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

#решение
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


# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#скрипт создающий директории
import os
work_dir = os.getcwd()
path = os.path.join(work_dir, 'dir_')
print('Скрипт создаст 9 директорий dir_1-dir_9 в рабочей папке')
try:
	for i in range(9):
		dir_name = path+str(i+1)
		os.mkdir(dir_name)
except FileExistsError:
	print('Папки с таким именем уже существуют')
except PermissionError:
	print('Не хватает прав доступа для этой операции')
else:
	print('В папке {} созданы новые директории dir_1-dir_9'.format(work_dir))
	
#скрипт удаляющий директории
import os
work_dir = os.getcwd()
path = os.path.join(work_dir, 'dir_')
print('Скрипт удалит 9 директорий dir_1-dir_9 из рабочей папки')
try:
	for i in range(9):
		dir_name = path+str(i+1)
		os.rmdir(dir_name)
except FileNotFoundError:
	print('Папок с именами dir1-dir9 не существует')
except PermissionError:
	print('Не хватает прав доступа для этой операции')
except OSError:
	print('Операция не может быть выполнена. Директории dir1-\
dir9 не пусты')
else:
	print('Из папки {} удалены  директории dir1-dir9'.format(work_dir))	
			

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
import os
work_dir = os.getcwd() #текущая директория

for root, dirs, files in os.walk(work_dir):
	folders = dirs
	break
	
print('Папки в рабочей директории: ')
for i in folders:
	print(i)

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil
work_dir = os.getcwd()  #текущая директория
src_file = os.path.join(work_dir, __file__)  #имя запущенного файла
dest_file = src_file + '_copy'  #имя копии запущенного файла 
shutil.copyfile(src_file, dest_file)  #создаём копию 
print('Создана копия текущего файла {} в файле {}'.format(src_file, dest_file))
