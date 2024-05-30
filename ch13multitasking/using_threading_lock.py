import threading
import time

#Lock, iş parçacıklarının aynı anda belirli bir kod parçasına erişmesini engellemek için kullanılır.
lock = threading.Lock()

def worker_thread(name):
    print(f'İş Parçacığı {name} kilit bekliyor')
    with lock:
        print(f'İş Parçacığı {name} kilidi aldı')
        time.sleep(2)
        print(f'İş Parçacığı {name} kilidi serbest bıraktı')

if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker_thread, args=(f'T{i}',))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('Ana iş parçacığı bitti')