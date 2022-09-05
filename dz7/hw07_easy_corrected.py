# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        #стороны
        self.ab = self.length_side(self.ax, self.ay, self.bx, self.by)
        self.bc = self.length_side(self.bx, self.by, self.cx, self.cy)
        self.ac = self.length_side(self.ax, self.ay, self.cx, self.cy)
        #периметр
        self.perimetr = self.perimetr(self.ab, self.bc, self.ac)
        #высота
        self.height = self.height(self.ab, self.bc, self.ac)
        #площадь
        self.area = self.area(self.ac, self.height)
        
    #высота треугольника       
    def height(self, a, b, c):
        p = (a + b + c) / 2
        return (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / a
        
    #длина отрезка
    def length_side (self, x1, y1, x2, y2):
        xy = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return xy
        
    #площадь тругольника     
    def area(self, height, ac):
        return ac * height / 2
        
    #периметр    
    def perimetr(self, a, b, c):
        return a + b + c

tr = Triangle(0, 0, 3, 5, 4, 0)
print('Периметр: {:.3}'.format(tr.perimetr))
print('Высота: {:.3}'.format(tr.height))
print('Площадь: {:.3}'.format(tr.area))
        


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math

class Trapezoid:
    def __init__(self, points_list):
        self.ax = points_list[0]
        self.ay = points_list[1]
        self.bx = points_list[2]
        self.by = points_list[3]
        self.cx = points_list[4]
        self.cy = points_list[5]
        self.dx = points_list[6]
        self.dy = points_list[7]
        #стороны
        self.ab = self.length_side(self.ax, self.ay, self.bx, self.by)
        self.bc = self.length_side(self.bx, self.by, self.cx, self.cy)
        self.cd = self.length_side(self.cx, self.cy, self.dx, self.dy)
        self.ad = self.length_side(self.ax, self.ay, self.dx, self.dy)
        #диагонали
        self.ac = self.length_side(self.ax, self.ay, self.cx, self.cy)
        self.bd = self.length_side(self.bx, self.by, self.dx, self.dy)  
        #периметр
        self.perimetr = self.ab + self.bc + self.cd + self.ad
        #высота
        self.height = math.sqrt((self.ab ** 2) - ((((self.ad - self.bc)\
** 2) / 4)) / 4)
        #площадь
        self.area = self.area(self.height, self.ad, self.bc)
        
    #длина отрезка
    def length_side (self, x1, y1, x2, y2):
        xy = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return xy
        
    #равнобокая или нет
    def is_equal(self):
        return self.ac == self.bd
            
    #площадь    
    def area(self, h, a, b):
        return h * (a + b) / 2


points = (0, 0, 2, 4, 4, 4, 6, 0)
tr = Trapezoid(points)
if tr.is_equal:
    print('Трапеция равнобедренная')
    print('Периметр = {:.3}'.format(tr.perimetr))
    print(('Стороны: ab = {0:.3}, bc = {1:.3}, cd = {2:.3}, ad = {3:.3}'
        .format(tr.ab, tr.bc, tr.cd, tr.ad))) 
    print('Высота = {:.3}'.format(tr.height))
    print('Площадь = {:.3}'.format(tr.area))
else:
    print('Трапеция не равнобедренная')



