#Создание классов автосалона и автомобиля. Салон имеет список автомобилей. Автомобиль имеет техн.характеристики и информацию о деталях, требующих ремонта.
#класс автосалона
class CarDealerShip:
    def __init__(self, nameInput):
        self.__carsList = []
        self.__name = nameInput
        self.__count = 0
        
    #получить список имеющихся автомобилей     
    @property
    def get_cars(self):
        return self.__carsList
    
    #Название автосалона 
    @property
    def name(self):
        return self.__name
    
    #количество автомобилей в списке автосалона
    @property
    def count(self):
        return self.__count
    
    #добавление автомобиля в список
    def add_car(self, car):
        self.__carsList.append(car)
        self.__count += 1
    
    #удаление автомобиля из списка
    def remove_car(self, car):
        self.__carsList.remove(car)
        self.__count -= 1 

#класс легкового автомобиля
class Car:
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
    
    #Вин номер
    @property
    def vin(self):
        return self.__vin
        
    @vin.setter
    def vin(self, vinInput):
        self.__vin = vinInput
    
    #Марка
    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, markInput):
        self.__mark = markInput
        
    #модель
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, modelInput):
        self.__model = modelInput
    
    #страна изготовления
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, countryInput):
        self.__country = countryInput
    
    #год выпуска
    @property
    def year(self):
        return self.__year  
                 		
    @year.setter
    def year(self, yearInput):
        self.__year = yearInput
    
    #объём двигателя
    @property
    def engine_volume(self):
        return self.__engineVolume    

    @engine_volume.setter
    def engine_volume(self, engineVolumeInput):
        self.__engineVolume = engineVolumeInput
    
    #пробег
    @property
    def mileage(self):
        return self.__mileage        

    @mileage.setter
    def mileage(self, mileageInput):
        self.__mileage = mileageInput
    
    #определение деталей, требующих ремонта - передаём список деталей в параметрах метода
    def add_for_repare(self, *args):   #список деталей требующих ремонта
        self.__repareNameList = args
        
    @property
    def repare_part_names(self):
        return self.__repareNameList
    
    
    
    #создаём объекты выбранных деталей, требующих ремонта и помещаем их в список
    def add_parts_to_repare(self):    #cписок объектов деталей треб.ремонта
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
    def repare_parts(self):
        return self.__reparePartList
     
    #стоимость автомобиля
    @property
    def car_cost(self):
        return self.__carCost
    
    #итоговая стоимость автомобиля с учётом ремонта 
    @property            
    def result_cost(self):
        if len(self.__reparePartList) > 0:
            for part in self.__reparePartList:
                self.__resultCost += part.cost
        else:
            self.__resultCost = self.__carCost
        return self.__resultCost
    
    #вывод информации 
    @property
    def info(self):
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

        
        
#грузовик на основе автомобиля
class Lorry(Car):
    def __init__(self, markInput, modelInput, countryInput, yearInput, 
                cost_input):
        self.__loadCapacity =  'undefined' 	
        super().__init__( markInput, modelInput, countryInput, yearInput, 
                cost_input)
    
    #для грузовика можно задать грузоподъёмность
    @property
    def load_capacity(self):
        return self.__loadCapacity

    @load_capacity.setter
    def load_capacity(self, loadCapacityInput):
        self.__loadCapacity = loadCapacityInput
    
    #вывод информации
    @property
    def info(self):
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
                print(f'({part.name}    {part.cost}')
        else:
            print('Машина технически исправна')
        print (f'Общая стоимость с учётом ремонта: {self.result_cost}')
        
        
#классы  деталей, требующих ремонта
class RepareParts:
    def __init__(self):
        self._name = ''
        self._cost = 0
    @property    
    def name(self):
        return self._name
    @property    
    def cost(self):
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
for car in salon.get_cars:
    print(car.mark, car.model, car.country, car.year)

lorry.add_for_repare('капот')
lorry.add_parts_to_repare()
lorry.info


