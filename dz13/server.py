#Использование модуля logging
from socket import socket, AF_INET, SOCK_DGRAM
import json
import time
import logging
import logging.config
import functools


server_address = ('localhost', 6789)
max_size = 1024
clients = {}  #словарь из адресов и имён клиентов

#создание логгера
logging.config.fileConfig(fname = 'log_config.py', disable_existing_loggers=False)
loggerServer = logging.getLogger('server' + __name__)

#создание декоратора
def log(decorated_function):
    functools.wraps(decorated_function)
    def wrapper(*args, **kwargs):
        loggerServer.debug(f'Вызываем функцию {decorated_function.__name__} из {__name__}')
        result = decorated_function(*args, **kwargs)
        loggerServer.debug(f'Функция {decorated_function.__name__} была вызвана из {__name__} с аргументами {args}{kwargs}')
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
  
print('Starting the server')
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(server_address)

#json ответ на основе json объекта, полученного от клиента
@log
def get_answer(client_json_message):
    message = client_json_message.get('message')
    name = client_json_message.get('user').get('name')
    time = get_time()
    code = 202
    json_message = {
            'responce':code,
            'time':time,
            'user':
                {
                'name':name,
                'status':'online'
                },
            'message':message
            }
    return json_message

while True:
        byte_data, client_address = server_socket.recvfrom(max_size)
            
        string_data = byte_data.decode('utf-8') #из байтов в строку
        json_data = json.loads(string_data) #из строки  в json
        
        #адрес и имя нового клиента добавляем в словарь clients
        if client_address not in list(clients.keys()):
            clients[client_address] = json_data.get('user').get('name')

        print(f"{json_data.get('user').get('name')} sent a message: {json_data.get('message')} at {get_time()}")
        
        #готовим ответ
        answer = get_answer(json_data)
        byte_answer = json.dumps(answer).encode('utf-8') #ответ в байты
        
        #если в адресатах 'all', пересылаем всем участникам чата
        if json_data.get('address') =='all':
            for client in list(clients.keys()):
                if client_address != client:
                    server_socket.sendto(byte_answer, client)
                    
        #если в адрестатах имя адресата, посылаем только адресату с этим именем
        if json_data.get('address') != 'all':
            if json_data.get('address') in list(clients.values()):
                for item in clients.items():
                    key, value = item
                    if value == json_data.get('address'):
                        server_socket.sendto(byte_answer, key)
                        
        #если от клинта  сообщение о выходе                 
        if json_data.get('message') == 'exit':
            print(f"{json_data.get('user').get('name')} disconnected at {get_time()}")
            del clients[client_address]
            
            
server_socket.close()



