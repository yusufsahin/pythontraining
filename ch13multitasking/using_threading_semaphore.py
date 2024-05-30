import threading
import time
#Semaphore, belirli sayıda iş parçacığının aynı anda belirli bir kaynağa erişmesini sağlar.
semaphore = threading.Semaphore(3)  # Aynı anda en fazla 3 iş parçacığı erişebilir
def worker_thread(name):
    print(f'İş Parçacığı {name} semafor bekliyor')
    with semaphore:
        print(f'İş Parçacığı {name} semaforu aldı')
        time.sleep(2)
        print(f'İş Parçacığı {name} semaforu serbest bıraktı')


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker_thread, args=(f'T{i}',))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('Ana iş parçacığı bitti')
