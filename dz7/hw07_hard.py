# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла



class Worker:
    def __init__(self, string_from_file, file_hour_path):
		#разбиваем строку в список и получаем все данные рабочего
        self.__name = string_from_file.split()[0]
        self.__surname = string_from_file.split()[1]
        self.__salary = float(string_from_file.split()[2])  #оклад
        self.__position = string_from_file.split()[3] 
        self.__plan_hours = int(string_from_file.split()[4])  #норма часов
        self.__file_hour_path = file_hour_path
        self.__fact_hours = self.get_fact_hours()  #фактически отработанные часы
        self.__salary_per_month = self.calculate() #зарплата за месяц
        
    #получаем фактически отработанные часы из файла           
    def get_fact_hours(self):
        with open (self.__file_hour_path, 'r') as f:
            string_hour_file = f.readline()  #первую строку файла (шапку таблицы) не будем считывать
            while True:
                string_hour_file = f.readline()        
                if len(string_hour_file) == 0:
                    break
                elif (self.name in string_hour_file) and (self.surname in string_hour_file):    
                    fact_hours = int(string_hour_file.split()[2])
                    break
        return fact_hours
        
    #расчёт зарплаты 
    def calculate(self):  
        salary_per_hour = self.__salary / self.__plan_hours	 #з.п. в час
        #если отработано меньше нормы
        if self.__fact_hours < self.__plan_hours:
            salary_per_month = salary_per_hour * self.__fact_hours   #з.п. за месяц
        #если отработано больше нормы, з.п. каждый лишний час оплачивается по двойному тарифу
        elif self.__fact_hours > self.__plan_hours:
            extra_hours = self.__fact_hours - self.__plan_hours #переработанные часы
            salary_per_month = self.__salary + 2 * salary_per_hour * extra_hours
        else:
            salary_per_month = self.__salary
        return salary_per_month	
        
    @property
    def name(self):
        return self.__name  
                      		 
    @property
    def surname(self):
        return self.__surname
    
    @property
    def position(self):
        return self.__position
    
    @property
    def salary(self):
        return self.__salary 
        
    @property
    def plan_hours(self):
        return self.__plan_hours
        
    @property
    def fact_hours(self):
        return self.__fact_hours
    @property
    def salary_per_month(self):
        return self.__salary_per_month   
        
workers_list = [] #список рабочих
path_to_hour_file = './data/hours_of'  #путь к файлу с часами
with open ('./data/workers', 'r') as f:
	#заполняем список рабочих
    string_workers_file = f.readline()  #первую файла строку (шапку таблицы) не будем считывать
    while True:
        string_workers_file = f.readline()
        if len(string_workers_file) == 0:
            break
        else:
            worker = Worker(string_workers_file, path_to_hour_file)
            workers_list.append(worker)


table_head = ['Имя', 'Фамилия', 'Оклад', 'Должность', 'Норма', 'Отработано', 'Зарплата']			
print('{0[0]:<10.15} {0[1]:<10.15} {0[2]:<10.15} {0[3]:<15} {0[4]:<10.15} {0[5]:<10.15} {0[6]:<10.15}'\
.format(table_head))
for worker in workers_list:
    print( '{0:<10.15} {1:<10.15} {2:<10} {3:<15} {4:<10} {5:<10} {6:<10.2f}'\
.format(worker.name, worker.surname, worker.salary, worker.position, worker.plan_hours,\
worker.fact_hours, worker.salary_per_month))

