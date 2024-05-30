#Event, bir iş parçacığının diğerini beklemesini sağlamak için kullanılır.
import threading
import time

event = threading.Event()

def worker_thread(name):
    print(f'İş Parçacığı {name} olay bekliyor')
    event.wait()
    print(f'İş Parçacığı {name} olay tetiklendi ve devam ediyor')

if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker_thread, args=(f'T{i}',))
        threads.append(t)
        t.start()

    print('Ana iş parçacığı 3 saniye bekliyor')
    time.sleep(3)
    print('Ana iş parçacığı olayı tetikliyor')
    event.set()

    for t in threads:
        t.join()

    print('Ana iş parçacığı bitti')
