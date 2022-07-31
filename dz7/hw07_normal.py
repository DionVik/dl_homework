# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self):
        self.__groups = [] #список групп в школе
        
    #добавление группы в школу     
    def add_group(self, input_group):
        self.__groups.append(input_group)
        
    #получить список групп в школе
    def get_groups(self):
        return self.__groups
		
    #получить список номеров групп в школе
    @property	
    def group_numbers(self):
        group_numbers_list = []
        for i in self.__groups:
            group_numbers_list = i.number
        return group_numbers_list
        	
class Group:
    def __init__(self, input_group_number):
        self.__number = input_group_number  #номер и буква класса
        self.__pupils = []  #ученики
        self.__teachers = []  #учителя
        
    #добавление ученика в группу    
    def add_pupil(self, input_pupil):
        self.__pupils.append(input_pupil)
   
    #добавление учителя в группу
    def add_teacher(self, input_teacher):
        self.__teachers.append(input_teacher)     
        
    #список фио учеников в группе
    @property
    def pupils(self):
        pupils_fio_list = []
        for pupil in self.__pupils:
            pupils_fio_list.append(pupil.fio)			
        return pupils_fio_list    	
        
    #список фио учителей в группе
    @property
    def teachers(self):
        teachers_fio_list = []
        for teacher in self.__teachers:
            teachers_fio_list.append(teacher.name)
        return teachers_fio_list
        
    #список предметов изучаемых в группе
    @property
    def subjects(self):
        subjects_list = []
        for teacher in self.__teachers:
            subjects_list.append(teacher.subject)
        return subjects_list
    
    #номер группы
    @property
    def number(self):
        return self.__number			
	
class Teacher:
    def __init__(self, teacher_fio_input, subject_input):
        self.__teacher_fio = teacher_fio_input
        self.__subject_name = subject_input
        
    #получить фио учителя    
    @property
    def name(self):
        return self.__teacher_fio
        
    #получить предмет учителя    
    @property
    def subject(self):
        return self.__subject_name
			
class Pupil:   
    def __init__(self, input_surname, input_name, input_parent_name):
        self.__surname = input_surname
        self.__name = input_name
        self.__parent_name = input_parent_name
        self.__fio = self.__surname + ' ' + (self.__name[0]).upper() +\
'.' + (self.__parent_name[0]).upper() + '.'
        self.__father_name = '' 
        self.__mother_name = ''
        self.__group = None 
   
    #получить школьные данные ученика 
    def get_school_data(self, school):
        for group in school.get_groups():
            if self.fio in group.pupils:
                self.__group = group
                
   	#получить номер группы
    @property
    def group_number(self):
        return self.__group.number	
		
    #получить список предметов изучаемых учеником
    @property
    def subjects(self):
        return self.__group.subjects
	
    #получить фио ученика    
    @property
    def fio(self):
        return self.__fio   
    
    #получить фио отца   
    @property
    def father(self):
        return self.__father_name   
            
    #задать фио отца            
    @father.setter
    def father(self, input_father_name):
        self.__father_name = input_father_name
             
    #получить фио матери   
    @property
    def mother(self):
        return self.__mother_name   
            
    #задать фио матери            
    @mother.setter
    def mother(self, input_mother_name):
        self.__mother_name = input_mother_name
       
#школа
school = School()  
      
#ученик 1		
pup1 = Pupil('Ефремов', 'Денис', 'Викторович')
print('ФИО ученика pup1: {}'.format(pup1.fio))	
pup1.father = 'Ефремов Виктор Михайлович'
print('Отец ученика {}: {}'.format(pup1.fio, pup1.father))
pup1.mother = 'Ефремова Лидия Александровна'
print('Мать ученика {}: {}'.format(pup1.fio, pup1.mother))


#ученик 2
pup2 = Pupil('Ридош', 'Ольга', 'Борисовна')
print('ФИО ученика pup2: {}'.format(pup2.fio))	
pup2.father = 'Ридош Борис Михайлович'
print('Отец ученика {}: {}'.format(pup2.fio, pup2.father))
pup2.mother = 'Ридош Наталья Семёновна'
print('Мать ученика {}: {}'.format(pup2.fio, pup2.mother))

#Учитель 1
teach1 = Teacher('Иванов С.А.', 'Русский язык')
teach2 = Teacher('Петров Д.А.', 'Математика')

#Группа 1а
gr1 = Group('1a')
gr1.add_pupil(pup1)
gr1.add_pupil(pup2)
gr1.add_teacher(teach1)
gr1.add_teacher(teach2)
print('Ученики группы {}: {}'.format(gr1.number, gr1.pupils))
print('Учителя группы {}: {}'.format(gr1.number, gr1.teachers))

school.add_group(gr1)
print('Группы в школе: {}'.format(school.group_numbers))

pup1.get_school_data(school)
print('Группа ученика {}: {}'.format(pup1.fio, pup1.group_number))
print('Предметы ученика {}: {}'.format(pup1.fio, pup1.subjects))
