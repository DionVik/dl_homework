
#класс автосалона
class CarDealerShip:
    def __init__(self, nameInput):
        self.__carsList = []
        self.__name = nameInput
        self.__count = 0
 
    @property
    def cars(self):
        '''Получить список имеющихся в салоне автомобилей'''
        return self.__carsList

    @property
    def name(self):
        '''Получить название автосалона'''
        return self.__name
     
    @property
    def count(self):
        '''Количество автомобилей'''
        return self.__count
    
    def add_car(self, car):
        '''Добавить автомобиль в салон'''
        self.__carsList.append(car)
        self.__count += 1
    
    def remove_car(self, car):
        '''Удалить автомобиль из салона'''
        self.__carsList.remove(car)
        self.__count -= 1 

class Car:
    '''Класс легкового автомобиля'''
    def __init__(self, markInput, modelInput, countryInput, yearInput, 
                cost_input):
        self.__vin = 'undefined'
        self.__mark = markInput
        self.__model = modelInput
        self.__country = countryInput
        self.__year = yearInput
        self.__engineVolume = 'undefined'
        self.__mileage = 'undefined'
        self.__carCost = cost_input
        self.__resultCost = self.__carCost
        self.__repareNameList = []  #список названий деталей требующих ремонта
        self.__reparePartList = []  #список объектов деталей требующих ремонта
        
    @property
    def vin(self):
        '''Получить ВИН номер автомобиля'''
        return self.__vin
        
    @vin.setter
    def vin(self, vinInput):
        '''Задать ВИН номер автомобиля'''
        self.__vin = vinInput
        
    @property
    def mark(self):
        '''Получить марку автомобиля'''
        return self.__mark

    @mark.setter
    def mark(self, markInput):
        '''Задать марку автомобиля'''
        self.__mark = markInput

    @property
    def model(self):
        '''Получить модель автомобиля'''
        return self.__model

    @model.setter
    def model(self, modelInput):
        '''Задать модель автомобиля'''
        self.__model = modelInput

    @property
    def country(self):
        '''Получить страну производителя автомобиля'''
        return self.__country

    @country.setter
    def country(self, countryInput):
        '''Задать страну производителя автомобиля'''
        self.__country = countryInput

    @property
    def year(self):
        '''Получить год выпуска автомобиля'''
        return self.__year  
                 		
    @year.setter
    def year(self, yearInput):
        '''Задать год выпуска автомобиля'''
        self.__year = yearInput

    @property
    def engine_volume(self):
        '''Получить объём двигателя'''
        return self.__engineVolume    

    @engine_volume.setter
    def engine_volume(self, engineVolumeInput):
        '''Задать объём двигателя'''
        self.__engineVolume = engineVolumeInput

    @property
    def mileage(self):
        '''Получить пробег'''
        return self.__mileage        

    @mileage.setter
    def mileage(self, mileageInput):
        '''Задать пробег'''
        self.__mileage = mileageInput
    
    def add_for_repare(self, *args):
        '''Добавить неисправные детали в список деталей требующих ремонта'''
        self.__repareNameList = args
    
    def add_parts_to_repare(self):
        '''Cписок объектов деталей требующих ремонта'''
        for name in self.__repareNameList:
            if name == 'двигатель':
                self.__reparePartList.append(Engine())
            elif name=='колесо':
                self.__reparePartList.append(Wheel())
            elif name=='сиденье':
                self.__reparePartList.append(Sit())
            elif name=='капот':
                self.__reparePartList.append(Capot())
     
    @property
    def car_cost(self):
        '''Получить стоимость автомобиля'''
        return self.__carCost
        
    @property            
    def result_cost(self):
        '''Получить конечную стоимость автомобиля'''
        if len(self.__reparePartList) > 0:
            for part in self.__reparePartList:
                self.__resultCost += part.cost
        else:
            self.__resultCost = self.__carCost
        return self.__resultCost
        
    @property
    def repare_parts(self):
        '''Список деталей, требующих ремонта'''
        return self.__reparePartList
    
    @property
    def repare_part_names(self):
        '''Список названий деталей, требующих ремонта'''
        return self.__repareNameList
    
    @property
    def info(self):
        '''Вывести информацию по автомобилю'''
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'VIN: {self.vin}')
        print(f'Страна производитель: {self.country}')
        print(f'Год выпуска: {self.year}')
        print(f'Объём двигателя: {self.engine_volume}')
        print(f'Пробег: {self.mileage}')
        print(f'Стоимость: {self.car_cost}')
        if len(self.repare_part_names) > 0:
            print('Требуют ремонта: ')
            for name in self.repare_part_names:
                print(name)
            print('Возможно заменить: ')
            for part in self.repare_parts:
                print(f'({part.name}    {part.cost}')
        else:
            print('Машина технически исправна')
        print (f'Общая стоимость с учётом ремонта: {self.result_cost}')


class Lorry(Car):
    '''Класс грузовика на основе класса автомобиля'''
    def __init__(self, markInput, modelInput, countryInput, yearInput, 
                cost_input):
        self.__loadCapacity =  'undefined' 	
        super().__init__( markInput, modelInput, countryInput, yearInput, 
                cost_input)

    @property
    def load_capacity(self):
        '''Получить грузоподъёмность'''
        return self.__loadCapacity

    @load_capacity.setter
    def load_capacity(self, loadCapacityInput):
        '''Задать грузоподъёмность'''
        self.__loadCapacity = loadCapacityInput
    
    @property
    def info(self):
        '''Вывести информацию по грузовику'''
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'VIN: {self.vin}')
        print(f'Страна производитель: {self.country}')
        print(f'Год выпуска: {self.year}')
        print(f'Объём двигателя: {self.engine_volume}')
        print(f'Пробег: {self.mileage}')
        print(f'Грузоподъёмность:{self.load_capacity}')
        print(f'Стоимость: {self.car_cost}')
        if len(self.repare_part_names) > 0:
            print('Требуют ремонта: ')
            for name in self.repare_part_names:
                print(name)
            print('Возможно заменить: ')
            for part in self.repare_parts:
                print(f'{part.name}  за  {part.cost}')
        else:
            print('Машина технически исправна')
        print (f'Общая стоимость с учётом ремонта: {self.result_cost}')
        
        
#классы  деталей, требующих ремонта
class RepareParts:
    '''Интерфейс деталей, требующих ремонта'''
    def __init__(self):
        self._name = ''
        self._cost = 0
    @property    
    def name(self):
        '''Получить название детали, требующей ремонта'''
        return self._name
    @property    
    def cost(self):
        '''Получить стоимость детали, требующей ремонта'''
        return self._cost


class Engine(RepareParts):
    def __init__(self):
        self._name = 'Двигатель'
        self._cost = 20000
    
    
class Wheel(RepareParts):
    def __init__(self):
        self._name = 'Колесо'
        self._cost = 5000
        
        
class Sit(RepareParts):
    def __init__(self):
        self._name = 'Сиденье'
        self._cost = 20000
        
class Capot(RepareParts):
    def __init__(self):
        self._name = 'Капот'
        self._cost = 2000

        
#создаём салон
salon = CarDealerShip('Скорость')
print(f'Добро пожаловать в наш автосалон подержанных автомобилей', 
    f'"{salon.name}"')
#создаём грузовик
lorry = Lorry('Zil', '130', 'Russia', '1980', 300000)
lorry.load_capacity = 10
lorry.vin = '90XBT16'
lorry.mileage = 240000
salon.add_car(lorry)
print(f'На данный момент в салоне находится {salon.count} машин. Это: ')
for car in salon.cars:
    print(car.mark, car.model, car.country, car.year)

lorry.add_for_repare('капот')
lorry.add_parts_to_repare()
lorry.info


