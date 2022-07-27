"""
    ПРИМЕЧАНИЕ: Для решения задачи необходимо познакомиться с модулями os, sys, argparse!
    СМ.: https://pythonworld.ru/moduli/modul-os.html,
    https://pythonworld.ru/moduli/modul-sys.html,
    https://habr.com/ru/company/ruvds/blog/440654/

    Задача похожа на задачу 2 из normal, однако, имеет особенности. Вы можете использовать решения из задачи 2.

    Задача:
    Напишите небольшую консольную утилиту, позволяющую работать с папками и файлами.
    Утилита должна работать с помощью параметров и флагов, передаваемых скрипту в командной строке.
    Примеры:
        python hw06_hard.py -touch ../dir1/test.txt -ls ../dir1/
        python hw06_hard.py -rm ../dir1/test.txt -ls ../dir1/
        python hw06_hard.py -mkdir ../dir1/newdir -ls ../dir1/
        python hw06_hard.py -ls ../dir1/
        python hw06_hard.py -touch ../dir1/test.txt

        и.т.д.

    Используйте модули argparse (для разбора аргументов), os, sys.

    Утилита должна принимать следующие флаги и выполнять следующие действия:
    "-ls <путь до папки>" - Посмотреть все файлы и подпапки в папке
    "-touch <путь до нового файла>" - Создать файл
    "-rm <путь до файла>" - Удалить файл
    "-mkdir <путь до папки>" - Создать папку

    Каждый из представленных параметров не обязательный, но если не указать никакой, то утилита должна вывести
    уведомление, которая предлагает посмотреть --help.
    Предусмотреть обработку исключений, например, если пытаются посмотреть все файлы не у папки, а у файла и.т.д.
"""
import sys
import os
import argparse

#создание экземпляра класса ArgumentParser.
parser = argparse.ArgumentParser()

#добавление параметров
parser.add_argument('-ls', type=str,  help='Просмотр содержимого каталога')
parser.add_argument('-touch', help='Создание нового файла') # type=argparse.FileType(mode='w', encoding='utf8'))
parser.add_argument('-rm', help='Удаление файла')
parser.add_argument('-mkdir', help='Создание нового каталога')

#объект который содержит все переданные параметры команд.строки
args = parser.parse_args(sys.argv[1:])
if args.ls:
    try:
        for i in os.listdir(args.ls): 
            print(i)
    except (FileNotFoundError, NotADirectoryError) as error:
        print(error)
if args.touch:
    try:
        f = open(args.touch, 'w', encoding='utf8')
        f.close()
    except IOError as error:
        print(error)
if args.rm:
    try:
        os.remove(args.rm)
    except FileNotFoundError as error:
        print(error)
if args.mkdir:
    os.mkdir(args.mkdir)
if args.ls == None and args.touch == None and args.rm == None and \
args.mkdir == None:
    print('Для получения справки введите параметр --help')
