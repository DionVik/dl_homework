# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Решение  задачи  без re.

lines = [
		'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm',
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV',
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA',
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV',
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW',
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC',
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR',
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm',
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn',
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS',
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf',
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH',
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN',
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ',
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
       ]
big_letters_list = list(map(chr, range(ord('A'),ord('Z')+1))) #список возможных больших букв

for source in lines:
	flag_last = False #Флаг конца строки
	result = []  #здесь будем хранить результат 
	small_str = '' #временная строка для маленьких букв
	big_str = ''  #временная строка для больших букв
	flag_small = False  #когда получена маленькая буква, flag_small= True
	for i in source:
		if source[-1]==i:
			flag_last = True
		if i in big_letters_list:
			flag_small = False				#получена большая буква
		else:
			flag_small = True            #получена маленькая буква
		if len(big_str) == 0 and flag_small == True:    
			small_str = small_str + i
		elif len(big_str) > 0 and len(small_str) >=2 and (flag_small == True or flag_last == True):  #Была строка больших букв и получена маленькая, либо достигнут конец строки 
			if len(big_str) >= 3:						   #Если строка больших букв больше 3, то сохраняем её в массив
				result.append(big_str[:-2])
				small_str = i
				big_str = ''
			else:									#Строка больших букв меньше 3, то 
				small_str = i                      #строка мал.букв = полученной букве
				big_str = ''                        #строка больших букв не подходит нам - обнуляем её 
		if len(small_str) > 0 and flag_small == False:
			if len(small_str) >=2:
				big_str = big_str + i
			else:
				small_str = ''
	print ('Для строки: {}, результат: {}'.format(source, result))
