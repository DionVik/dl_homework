# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Решение задачи без re.

lines = [
		'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO',
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK',
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn',
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa',
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete',
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ',
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb',
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC',
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB',
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT',
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu',
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB',
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa',
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ',
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
       ]
big_letters_list = list(map(chr, range(ord('A'), ord('Z')+1)))   #список больших букв
       
for source in lines:
	result_list = []   #список, куда будем помещать найденные строки из маленьких букв
	small_str ='' #строка маленьких букв
	flag_small = False  #если получена маленькая буква flag_samll = True
	for i in source: 
	    if i not in big_letters_list:      #если получена маленькая буква
	        flag_small = True                       #устанавливаем флаг    
	    else:
	        flag_small = False                       #если буква большая - флаг сбрасываем
	    if flag_small:
	        small_str = small_str + i     #если буква маленькая, помещаем её во временную строку
	    elif flag_small == False and len(small_str) > 0:         #если маленькая буква сменилась на большую 
	        result_list.append(small_str)                      #добавляем строку в список
	        small_str = ''                                             #обнуляем временную строку  
	    else:
	        flag_small = False
	if len(small_str)>0:                      #если маленькие буквы завершают строку line (после них больше нет больших букв)                 
	    result_list.append(small_str)         #помещаем в список последнюю строку маленьких букв
	print('Для строки: {}, результат: {}'.format(source, result_list))

