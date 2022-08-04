#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
 
class Card:
    def __init__(self, list_input, card_string_len):
        #отсортированные списки из 5 случайных чисел
        self.__random_num_list1 = self.sort_list(list_input[0:5])     
        self.__random_num_list2 = self.sort_list(list_input[5:10])   
        self.__random_num_list3 = self.sort_list(list_input[10:15])
        #длина строки в карте    
        self.__card_string_len = card_string_len          
        #строки с пробелами
        self.__card_string1 = self.get_space_list(self.__random_num_list1, self.__card_string_len)
        self.__card_string2 = self.get_space_list(self.__random_num_list2, self.__card_string_len)
        self.__card_string3 = self.get_space_list(self.__random_num_list3, self.__card_string_len)
    
        
    #сортировка списка        
    @staticmethod    
    def sort_list(lst):
        sorted_list = lst[:]
        for i in range(len(sorted_list)):
            for j in range(len(sorted_list)-1-i):
                if sorted_list[j] > sorted_list[j+1]:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1],\
sorted_list[j]
        return sorted_list
        
    #поиск значения в карте 
    def exist_value(self, value_input):
        flag = False
        for i in range(self.__card_string_len):
            if self.__card_string1[i] == value_input:
                flag =  True
                return flag
            elif self.__card_string2[i] == value_input:
                flag =  True
                return flag
            elif self.__card_string3[i] == value_input:
                flag =  True
                return flag
        return flag
    
    #Карта заполнена?
    def is_full(self):
        flag = True
        for i in range(self.__card_string_len):
            if self.__card_string1[i] != '-':
                flag =  False
                return flag
            elif self.__card_string2[i] != '-':
                flag =  False
                return flag
            elif self.__card_string3[i] != '-':
                flag =  False
                return flag
        return flag

    #рисование линии
    @staticmethod
    def draw_line():  
        print('{:-^36}'.format('-'))
        print()

    #рисование описания
    @staticmethod
    def draw_description(description):
        print('{:-^36}'.format(description))
    
    #получаем строку карты из  случайных чисел с пробелами    
    @staticmethod
    def get_space_list(num_list, list_len):
        card_string = [' ' for i in range(list_len)] #список с пробелами
        count = 0
        while count < len(num_list):
            i = random.randint(0, len(card_string)-1)
            if card_string[i] == ' ':
                card_string[i] = 'a'
                count += 1
        index = 0
        while index < len(num_list):
            for j in range(len(card_string)):
                if card_string[j] == 'a':
                    card_string[j] = num_list[index]
                    index += 1
                    break
        return card_string
    
    #рисование карты    
    def show(self, description):
        self.draw_description(description) #описание           
        print('{0[0]:^4}{0[1]:^4}{0[2]:^4}{0[3]:^4}{0[4]:^4}{0[5]:^4}{0[6]:^4}{0[7]:^4}{0[8]:^4}'.\
format(self.__card_string1))        
        print('{0[0]:^4}{0[1]:^4}{0[2]:^4}{0[3]:^4}{0[4]:^4}{0[5]:^4}{0[6]:^4}{0[7]:^4}{0[8]:^4}'.\
format(self.__card_string2))
        print('{0[0]:^4}{0[1]:^4}{0[2]:^4}{0[3]:^4}{0[4]:^4}{0[5]:^4}{0[6]:^4}{0[7]:^4}{0[8]:^4}'.\
format(self.__card_string3))
        self.draw_line()  #линия
    
    #зачёркивание числа        
    def delete_num(self, num_input):
        for i in range(self.__card_string_len):
            if self.__card_string1[i] == num_input:
                self.__card_string1[i] = 'X'
            if self.__card_string2[i] == num_input:
                self.__card_string2[i] = 'X'
            if self.__card_string3[i] == num_input:
                self.__card_string3[i] = 'X'

#список из случайных чисел   
def get_random_digits(quantity):
    random_digit_list = []
    count = 0
    while count != quantity:
        digit = random.randint(1, 20)
        if digit not in random_digit_list:
            random_digit_list.append(digit)
            count += 1
    return random_digit_list



def main():
    card_string_len = 9 #длина строки карты
    user_card = Card(get_random_digits(15), card_string_len) #карта пользователя
    pc_card = Card(get_random_digits(15), card_string_len)  #карта пк 
    used_values = []  #уже выпавшие значения
    step = 1  #счётчик ходов
    max_value = 20
    pc_win = False   #флаг выигрыша пк
    user_win = False  #флаг выигрыша пользователя
    end = False  #флаг конца игры
    	
    while step <= max_value and end == False:
        value = random.randint(1, max_value)  #вытаскиваем бочонок
        if value not in used_values:
            used_values.append(value)
            print('Новый бочонок: {} (осталось {})'.format(value, max_value - step))

             #отображаем карты
            user_card.show('Ваша карточка')
            pc_card.show('Карточка компьютера') 

            #проверяем значение на карте пк и зачёркиваем если оно есть
            if pc_card.exist_value(value):
                pc_card.delete_num(value)

            #ввод пользователя
            answer = ' '
            while answer != 'y' or answer != 'n':
                answer = input('Зачеркнуть число? (y/n)')
                if answer == 'y':
                    if user_card.exist_value(value):
                        user_card.delete_num(value)
                    else:
                        end = True
                        user_win = False
                    break
                elif answer == 'n':
                    if user_card.exist_value(value):
                        end = True
                        user_win = False
                    break     
                else:
                    print ("Введите 'y' или 'n'")

            #отображаем карты
            user_card.show('Ваша карточка')
            pc_card.show('Карточка компьютера')
            
            #заполнены ли карты?
            if pc_card.is_full():
                pc_win = True
                end = True
            if user_card.is_full():
                user_win = True
                end = True

            step += 1                           
    if pc_win:
        print('Компьютер выиграл')
    elif user_win:
        print('Вы выиграли')                    
    else:
        print('Вы проиграли')
            
if __name__ == '__main__':
    main()
                    
       
