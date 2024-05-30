import threading
import time

def worker_thread(name):
    print(f'İş parçacağı {name} başladı')
    time.sleep(2)
    print(f'İş parçacağı {name} bitti')

if __name__ == '__main__':
    print('Ana iş parçacığı başladı')

    threads=[]
    for i in range(5):
        t= threading.Thread(target=worker_thread, args=(f'T{i}',))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('Ana iş parçacığı')

#Süreçler ve İş Parçacıkları Arasındaki Farklar
#Süreçler:

#Her süreç kendi bağımsız bellek alanına sahiptir.
#Süreçler arasında veri paylaşımı genellikle zordur.
#Süreçler daha ağırdır, çünkü her süreç ayrı bir bellek alanı gerektirir.
#Süreçler, çok çekirdekli işlemcilerden tam olarak yararlanabilir.

#İş Parçacıkları:

#İş parçacıkları aynı bellek alanını paylaşır.
#İş parçacıkları arasında veri paylaşımı daha kolaydır, ancak senkronizasyon sorunlarına dikkat edilmelidir.
#İş parçacıkları daha hafiftir.
#İş parçacıkları, Global Interpreter Lock (GIL) nedeniyle Python'da sınırlı paralellik sağlar.
# Ancak I/O-bound işlemler için uygundur.