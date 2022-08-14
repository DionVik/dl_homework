# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# def fibonacci(n, m):
    # pass

#функция, возвращающая список чисел Фибоначчи в количестве от n до m
def fib(n, m):
    fibonachi_list=[1, 1] #список для чисел Фибоначчи
    for i in range(m-2):
        fibonachi_list.append(fibonachi_list[-1] + fibonachi_list[-2]) 
    return(fibonachi_list[n:]) #возвращаем список от n элемента 
    
n = int(input('Введите нижний предел ряда Фибоначчи: '))
m = int(input('Введите верхний предел ряда Фибоначчи: '))
print ('Ряд Фибоначчи от {} элемента до {}: {}'.format(n, m, fib(n, m)))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(origin_list):
    # pass

# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

#функция сортирующая список по возрастанию
def sort_to_max(lst):
    for i in range(0, len(lst)-1):
        for j in range(0, len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
    
lst = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print('Оригинальный список: ', lst)
print('Отсортированный список: ', sort_to_max(lst))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

#реализация функции filter
#применяет функцию к элементам последовательности и возвращает последовательность из элементов,
# для которых функция возвратит True
def my_filter(funk, lst):
    result=[]
    for i in lst:
        if funk(i):
            result.append(i)
    return result
        
spisok = [1, 2, 3, 4, 5]
#функция проверки чётности числа для примера
def proverka_chetnosti(el):
    if el%2 == 0:
        return True
    else:
        return False

a= my_filter(proverka_chetnosti, spisok)

print('Для списка {} и функции проверки чётности применим функцию my_filter'.format(spisok))
print ('Результат: {}'.format(a))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

#функция проверяет список координат точек в разных комбинациях их 
#расположения, т.к. не известно какая точка имеет нулевую координату
def check(lst):
    for i in range(4):
        print('lst=', lst)
        #координаты Y у расположенных рядом по горизонтали точек должны
        # быть равны
        if(lst[0][1] == lst[3][1]) and (lst[1][1] == lst[2][1]): 
            #смещения у верхних и нижних точек по X должны быть равны
            if (lst[1][0] - lst[0][0]) == (lst[2][0] - lst[3][0]): 
                return True
        lst=lst[-1:] + lst[:-1] #сдвигаем элементы массива на 1 шаг влево,
        #чтобы проверить следующую комбинацию расположения точек
    return False

a=[]
b=[]
c=[]
d=[]
a.append(int(input('Введите координату x точки А: ')))
a.append(int(input('Введите координату y точки А: ')))
b.append(int(input('Введите координату x точки B: ')))
b.append(int(input('Введите координату y точки B: ')))
c.append(int(input('Введите координату x точки C: ')))
c.append(int(input('Введите координату y точки C: ')))
d.append(int(input('Введите координату x точки D: ')))
d.append(int(input('Введите координату y точки D: ')))
lst=[a, b, c, d]  #список координат точек

if check(lst):
    print ('Эти точки являются точками параллелограмма')
else:
    print ('Эти точки не являются точками параллелограмма')



