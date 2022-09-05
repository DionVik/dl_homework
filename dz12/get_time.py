import time
def get_time():
    '''Получение текущего времени в формате чч:мм:сек'''
    time_object = time.time()
    current_time = (
        str(time.localtime(time_object)[3]) + ':' + 
        str(time.localtime(time_object)[4]) + ':' +
        str(time.localtime(time_object)[5])
    )
    return current_time
