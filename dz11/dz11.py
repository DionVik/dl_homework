import threading
import time

cv = threading.Condition()
book = ''

def writer1(interval):
    global book
    while True:
        try:
            cv.acquire()
            book = book + ' писатель1 '
            print('Писатель1 написал текст')
            cv.notify_all()
        finally:
            cv.release()
        time.sleep(interval)

def writer2(interval):
    global book
    while True:
        try:
            cv.acquire()
            book = book + ' писатель2 '
            print('Писатель2 написал текст')
            cv.notify_all()
        finally:
            cv.release()
        time.sleep(interval)

def reader1(interval):
    global book
    while True:
        try:
            cv.acquire()
            while True:
                cv.wait()
                a = book
                print(f'Читатель1 прочитал текст: {book}')
        finally:
            cv.release()
        time.sleep(interval)
        
def reader2(interval):
    global book
    while True:
        try:
            cv.acquire()
            while True:
                cv.wait()
                a = book
                print(f'Читатель2 прочитал текст: {book}')
        finally:
            cv.release()
        time.sleep(interval)
            
if __name__ == '__main__':        
    t1 = threading.Thread(target = writer1, name = 't1', args = (6,))
    t2 = threading.Thread(target = writer2, name = 't2', args = (6,))
    t3 = threading.Thread(target = reader1, name = 't3', args = (6,))
    t4 = threading.Thread(target = reader2, name = 't4', args = (6,))
    t1.daemon = True
    t2.daemon = True
    t3.daemon = True
    t4.daemon = True
    t4.start()   
    t3.start()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

