# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_list1 = ['арбуз', 'дыня', 'гранат']
fruits_list2 = ['груша', 'слива', 'дыня', 'арбуз', 'абрикос']

result_list = [i for i in fruits_list1 if  i in fruits_list2]

print ('Исходный список 1: {}'.format(fruits_list1))
print ('Исходный список 2: {}'.format(fruits_list2))
print('Элементы, присутствующие в обоих списках: {}'.format(result_list))          
