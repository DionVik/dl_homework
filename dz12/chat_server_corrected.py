from socket import socket, AF_INET, SOCK_DGRAM
import json
import time
from get_time import get_time

server_address = ('localhost', 6789)
max_size = 1024
clients = {}  #словарь адреса: имя клиента

#json ответ на основе json объекта полученного от клиента
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

def main():
    
    print('Starting the server')
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(server_address)
    
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

if __name__ == '__main__':
    main()



