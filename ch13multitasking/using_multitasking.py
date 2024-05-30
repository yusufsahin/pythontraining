import multiprocessing
import os

def child_process():
    print("Bu bir çocuk süreci")

if __name__ == "__main__":
    print(f"Bu ana süreç.Süreç ID'si {os.getpid()}")
    p=multiprocessing.Process(target=child_process)
    p.start()
    p.join()
    print(f"Bu ana süreç. Çocuk süreci ID'si: {p.pid}")