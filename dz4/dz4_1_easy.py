def convert(km):
	print('{0} км = {1:.2f} миль'.format(km, km*1.609))

km = float(input('Введите расстояние в км: '))
convert(km)

