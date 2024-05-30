import threading
import time

rlock = threading.RLock()
def worker_thread(name):
    print(f'İş Parçacığı {name} kilit bekliyor')
    with rlock:
        print(f'İş Parçacığı {name} kilidi aldı')
        with rlock:
            print(f'İş Parçacığı {name} tekrar kilidi aldı')
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
