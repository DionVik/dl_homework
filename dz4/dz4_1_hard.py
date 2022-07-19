import math  #библиотека понадобится для получения наиб.общ.делителя

def calc(stroka):
	"""Функция выделяет целые части, числители и знаменатели в выражении. 
	Аргумент - строка выражения.
	Возврат - словарь из знака, целой части, числителя 
	и знаменателя каждого слагаемого.
	"""
	# получаем список из слагаемых в зависимости от знака 
	if ' + ' in stroka: 
		znak = '+'
		lst = stroka.split(' + ')
	elif ' - ' in stroka:
		znak = '-'
		lst = stroka.split(' - ')
	slagaemoe1 = lst[0].strip() #слагаемое 1 в виде строки 
	slagaemoe2 = lst[1].strip() #слагаемое 2 в виде строки
	
	if '-' in slagaemoe1:
		znak_slagaemoe1 = -1
	else:
		znak_slagaemoe1 = 1
	if ('-' in slagaemoe2):
		znak_slagaemoe2 = -1
	else:
		znak_slagaemoe2 = 1
		
	#выделяем целую и дробную часть из слагаемых
	#если есть целая  и дробная части в 1 слагаемом
	if (' ' in slagaemoe1) and ('/' in slagaemoe1):  
		slagaemoe_list1 = slagaemoe1.split(' ')
		cel1 = int(slagaemoe_list1[0])  #целая часть 1 слагаемого
		drob1 = slagaemoe_list1[1]  
		ch1 = znak_slagaemoe1*abs(int(drob1.split('/')[0]))  #числитель 1 слагаемого
		zn1 = int(drob1.split('/')[1]) #знаменатель 1 слагаемого
		
		#избавляемся от целой части
		ch1 = cel1*zn1+ch1
		
	elif (' ' not in slagaemoe1) and ('/' in slagaemoe1): #если есть только дробная часть 
		cel1=0
		ch1 = znak_slagaemoe1 * abs(int(slagaemoe1.split('/')[0])) #числитель 1 слагаемого 
		zn1 = int(slagaemoe1.split('/')[1]) #знаменатель 1 слагаемого	
	else: #если нет пробеллов и знаков дроби - слагаемое = целому числу
		cel1 =int(slagaemoe1)
		ch1 = int(slagaemoe1)
		zn1 = 1
	
	#если есть целая  и дробная части во 2 слагаемом
	if (' ' in slagaemoe2) and ('/' in slagaemoe2):  
		slagaemoe_list2 = slagaemoe2.split(' ')
		cel2 = int(slagaemoe_list2[0])  #целая часть 1 слагаемого
		drob2 = slagaemoe_list2[1]  
		ch2 = znak_slagaemoe2 * abs(int(drob2.split('/')[0]))  #числитель 1 слагаемого
		zn2 = int(drob2.split('/')[1]) #знаменатель 1 слагаемого
		
		#избавляемся от целой части
		ch2 = cel2*zn2+ch2
	#если есть только дробная часть 
	elif (' ' not in slagaemoe2) and ('/' in slagaemoe2): 
		cel2=0
		ch2 = znak_slagaemoe2 * abs(int(slagaemoe2.split('/')[0])) #числитель 1 слагаемого 
		zn2 = int(slagaemoe2.split('/')[1]) #знаменатель 1 слагаемого	
	#если нет пробеллов и знаков дроби - слагаемое = целому числу
	else: 
		cel2 = int(slagaemoe2)
		ch2= int(slagaemoe2)
		zn2=1
	
	#если есть дробная часть в обоих слагаемых приводим дроби к общему знаменателю	
	if (zn1 and zn2):	
		nod_zn = math.gcd(zn1, zn2) #наибольший общий делитель для знаменателей
		nok = (zn1*zn2)/ nod_zn  #наименьшее общее кратное для знаменателей
		dop_mn1 = nok/zn1 #дополнительный множитель 1 слагаемого
		dop_mn2 = nok/zn2 #дополнительный множитель 2 слагаемого
	#для приведения к общему знаменателю умножаем числ.и знам. на доп. множитель
		ch1=ch1*dop_mn1  
		ch2 = ch2*dop_mn2
		zn = int(zn1*dop_mn1)  #общий знаменатель дробей
	elif (zn1 != 0 and zn2 ==0):
		zn = zn1
	else:
		zn = zn2
		
	#суммируем или вычитаем в зависимости от знака и получаем числитель и целую часть
	if znak == '+':
		ch = int(ch1+ch2)  #числитель дроби
		#cel = cel1+cel2 #целая часть дроби
	elif znak == '-':
		ch = int(ch1-ch2) #числитель дроби
		#cel = cel1-cel2 #целая часть дроби
	
	#если числитель больше знаменателя - увеличиваем целую часть и вычисляем новый числитель
	if abs(ch) > zn:
		cel = int(ch/zn)
		# вычисляем числитель как остаток деления по модулю. Операция % работает для положит. и отр. чисел по разному
		if ch > 0:
			ch = ch % zn
		else:
			ch = -1 * (abs(ch)%zn)
		
	#упрощаем дробную часть
	nod_ch_zn = math.gcd(ch,zn) #наибольший общий делитель числителя и знаменателя
	ch = int(ch / nod_ch_zn)
	zn = int(zn / nod_ch_zn)
	
	# возвращаем результат
	if cel == 0:
		result = str(ch)+'/'+str(zn)
	elif ch == 0:
		result = str(cel)
	else:
		result = str(cel)+' '+str(abs(ch))+'/'+str(zn)
	return result
	
	
s='-11/32 - -12 2/16'
print('Исходное выражение: {}'.format(s))
print('{} = {}'.format(s, calc(s)))

 


	
