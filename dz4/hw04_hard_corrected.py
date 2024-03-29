# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import math  #библиотека понадобится для получения наиб.общ.делителя

def calc(stroka):
    """Функция выделяет целые части, числители и знаменатели в выражении. 
    Аргумент - строка выражения.
    Возврат - словарь из знака, целой части, числителя 
    и знаменателя каждого слагаемого.
    """
    # получаем список из слагаемых в зависимости от знака 
    if ' + ' in stroka: 
        znak = '+'
        lst = stroka.split(' + ')
    elif ' - ' in stroka:
        znak = '-'
        lst = stroka.split(' - ')
    slagaemoe1 = lst[0].strip() #слагаемое 1 в виде строки 
    slagaemoe2 = lst[1].strip() #слагаемое 2 в виде строки

    if '-' in slagaemoe1:
        znak_slagaemoe1 = -1
    else:
        znak_slagaemoe1 = 1
    if ('-' in slagaemoe2):
        znak_slagaemoe2 = -1
    else:
        znak_slagaemoe2 = 1

    #выделяем целую и дробную часть из слагаемых
    #если есть целая  и дробная части в 1 слагаемом
    if (' ' in slagaemoe1) and ('/' in slagaemoe1):  
        slagaemoe_list1 = slagaemoe1.split(' ')
        cel1 = int(slagaemoe_list1[0])  #целая часть 1 слагаемого
        drob1 = slagaemoe_list1[1]  
        ch1 = znak_slagaemoe1*abs(int(drob1.split('/')[0]))  #числитель 1 слагаемого
        zn1 = int(drob1.split('/')[1]) #знаменатель 1 слагаемого
    
        #избавляемся от целой части
        ch1 = cel1 * zn1 + ch1
    
    elif (' ' not in slagaemoe1) and ('/' in slagaemoe1): #если есть только дробная часть 
        cel1 = 0
        ch1 = znak_slagaemoe1 * abs(int(slagaemoe1.split('/')[0])) #числитель 1 слагаемого 
        zn1 = int(slagaemoe1.split('/')[1]) #знаменатель 1 слагаемого	
    else: #если нет пробеллов и знаков дроби - слагаемое = целому числу
        cel1 =int(slagaemoe1)
        ch1 = int(slagaemoe1)
        zn1 = 1
    
    #если есть целая  и дробная части во 2 слагаемом
    if (' ' in slagaemoe2) and ('/' in slagaemoe2):  
        slagaemoe_list2 = slagaemoe2.split(' ')
        cel2 = int(slagaemoe_list2[0])  #целая часть 1 слагаемого
        drob2 = slagaemoe_list2[1]  
        ch2 = znak_slagaemoe2 * abs(int(drob2.split('/')[0]))  #числитель 1 слагаемого
        zn2 = int(drob2.split('/')[1]) #знаменатель 1 слагаемого
        
        #избавляемся от целой части
        ch2 = cel2 * zn2 + ch2
    #если есть только дробная часть 
    elif (' ' not in slagaemoe2) and ('/' in slagaemoe2): 
        cel2 = 0
        ch2 = znak_slagaemoe2 * abs(int(slagaemoe2.split('/')[0])) #числитель 1 слагаемого 
        zn2 = int(slagaemoe2.split('/')[1]) #знаменатель 1 слагаемого	
    #если нет пробеллов и знаков дроби - слагаемое = целому числу
    else: 
        cel2 = int(slagaemoe2)
        ch2= int(slagaemoe2)
        zn2=1
    
    #если есть дробная часть в обоих слагаемых приводим дроби к общему знаменателю	
    if (zn1 and zn2):	
        nod_zn = math.gcd(zn1, zn2) #наибольший общий делитель для знаменателей
        nok = (zn1*zn2)/ nod_zn  #наименьшее общее кратное для знаменателей
        dop_mn1 = nok/zn1 #дополнительный множитель 1 слагаемого
        dop_mn2 = nok/zn2 #дополнительный множитель 2 слагаемого
    #для приведения к общему знаменателю умножаем числ.и знам. на доп. множитель
        ch1=ch1 * dop_mn1  
        ch2 = ch2 * dop_mn2
        zn = int(zn1 * dop_mn1)  #общий знаменатель дробей
    elif (zn1 != 0 and zn2 == 0):
        zn = zn1
    else:
        zn = zn2
    
    #суммируем или вычитаем в зависимости от знака и получаем числитель и целую часть
    if znak == '+':
        ch = int(ch1 + ch2)  #числитель дроби
        #cel = cel1 + cel2 #целая часть дроби
    elif znak == '-':
        ch = int(ch1 - ch2) #числитель дроби
        #cel = cel1 - cel2 #целая часть дроби
    
    #если числитель больше знаменателя - увеличиваем целую часть и вычисляем новый числитель
    if abs(ch) > zn:
        cel = int(ch / zn)
        # вычисляем числитель как остаток деления по модулю. Операция % работает для положит. и отр. чисел по разному
        if ch > 0:
            ch = ch % zn
        else:
            ch = -1 * (abs(ch) % zn)
    
    #упрощаем дробную часть
    nod_ch_zn = math.gcd(ch, zn) #наибольший общий делитель числителя и знаменателя
    ch = int(ch / nod_ch_zn)
    zn = int(zn / nod_ch_zn)
    
    # возвращаем результат
    if cel == 0:
        result = str(ch) + '/' + str(zn)
    elif ch == 0:
        result = str(cel)
    else:
        result = str(cel) + ' ' + str(abs(ch)) + '/' + str(zn)
    return result
    
    
s = '-11/32 - -12 2/16'
print('Исходное выражение: {}'.format(s))
print('{} = {}'.format(s, calc(s)))

 
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

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
table_head = ['Имя', 'Фамилия', 'Оклад', 'Должность', 'Норма', 'Отработано', 'Зарплата']			
print( '{0[0]:<10.15} {0[1]:<10.15} {0[2]:<10.15} {0[3]:<15} {0[4]:<10.15} {0[5]:<10.15} {0[6]:<10.15}'.format(table_head))
for i in result_lst:
    print( '{0[0]:<10.15} {0[1]:<10.15} {0[2]:<10.15} {0[3]:<15} {0[4]:<10.15} {0[5]:<10.15} {0[6]:<10.2f}'.format(i))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

#Программа создания файлов для списков слов начинающихся с одинаковой буквы
#читаем все слова из файла fruits в список main_lst
with open('fruits.txt', 'r', encoding = 'utf8') as f:
    main_lst = [line for line in f if line != '\n']
#создаём список первых букв
first_letter_lst =  list(map(chr, range(ord('А'), ord('Я')+1)))
print(first_letter_lst)

#для каждой буквы из списка первых букв ищем слова начинающиеся с этой
#буквы, помещаем их во временный список и записываем в файл
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

        




