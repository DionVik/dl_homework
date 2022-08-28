#Использование модуля logging
from socket import socket, AF_INET, SOCK_DGRAM
import json
import time
import threading
import logging
import logging.config
import functools

server_address = ('localhost', 6789)
max_size = 1024
shutdown = False #флаг завершения

#создание логгера
logging.config.fileConfig(fname = 'log_config.py', disable_existing_loggers=False)
loggerClient = logging.getLogger('client' + __name__)

#создание декоратора
def log(decorated_function):
    functools.wraps(decorated_function)
    def wrapper(*args, **kwargs):
        loggerClient.debug(f'Вызываем функцию {decorated_function.__name__} из {__name__}')
        result = decorated_function(*args, **kwargs)
        loggerClient.debug(f'Функция {decorated_function.__name__} была вызвана из {__name__} с аргументами {args}{kwargs}')
        return result
    return wrapper

@log
def get_time():
    time_object = time.time()
    current_time = (
    str(time.localtime(time_object)[3]) + ':' + 
    str(time.localtime(time_object)[4]) + ':' +
    str(time.localtime(time_object)[5])
    )
    return current_time
@log
def json_data_for_sending(name, message, address):
    json_object = {
        'action':'msg_from_chat',
        'time':get_time(),
        'message':message,
        'user':
            {
            'name': name,
            'status':'online'
            },
        'address':address
        }
    return json_object
    
@log
def receving(socket, buffer_size):
    global shutdown
    while not shutdown:
        byte_data, server = socket.recvfrom(buffer_size)
        string_data = byte_data.decode('utf-8') #байты в строку
        json_object = json.loads(string_data)  #строку в словарь
        print(json_object.get('user').get('name') + '::',end='')
        print(json_object.get('message'))
        time.sleep(0.2)
        
print('Starting client')
client_socket = socket(AF_INET, SOCK_DGRAM)

name = input('Your name: ')
address = input('Chat with: ')

#уведомление о подключении
json_message = json_data_for_sending(name, 'Connected to server', address)
byte_message = json.dumps(json_message).encode('utf-8') #json в строку и в байты
client_socket.sendto(byte_message, server_address)

receving_thread = threading.Thread(target = receving, args = (client_socket, max_size),
daemon = True)
receving_thread.start()

while not shutdown:
    message = input('You::')
    if message != '':
        if message == 'exit':
            shutdown = True
        json_message = json_data_for_sending(name, message, address)
        byte_message = json.dumps(json_message).encode('utf-8') #json в строку и в байты
        client_socket.sendto(byte_message, server_address)
        time.sleep(0.2)
        
client_socket.close()



