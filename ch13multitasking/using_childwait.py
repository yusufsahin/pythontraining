import multiprocessing
import os
import time

def child_process():
    print("Çocuk süreci başladı.")
    time.sleep(5)  # Çocuk süreci 5 saniye boyunca çalışır
    print("Çocuk süreci bitti.")


if __name__ == '__main__':
    print(f"Ana süreç başladı. Süreç ID'si: {os.getpid()}")
    # Çocuk süreci oluştur ve başlat
    p = multiprocessing.Process(target=child_process)
    p.start()
    print(f"Bu ana süreç. Çocuk süreci başlatıldı. Çocuk süreci ID'si: {p.pid}")
    # Ana süreç, çocuk sürecin bitmesini bekler
    p.join()
    print("Ana süreç: Çocuk süreci tamamlandı.")


