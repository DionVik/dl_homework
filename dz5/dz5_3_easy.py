# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

number_list= [11, 6, 8, -222, 9, -12]
result_list = [i for i in number_list if (i % 3 == 0) and (i > 0) and (i % 4 != 0)]

print('Исходный список: {}'.format(number_list))
print('Список из элементов кратных 3, больше 0 и некратных 4: {}'.format(result_list))          