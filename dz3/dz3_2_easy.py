list1 = [1,2,3,4,5]
list2 = [16,30,3,8,4]
print('Список1: {}'.format(list1))
print('Список2: {}'.format(list2))

#создаём множества из списков
m1 = set(list1)
m2 = set(list2)
print('Из списка1 будут удалены элементы:{}'.format(m1 & m2))
m1 = m1-m2   # находим разность между множествами
list1 = list(m1) #преобразуем множество в список

print('Список1: {}'.format(list1))
print('Список2: {}'.format(list2))
