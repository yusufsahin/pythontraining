import multiprocessing

def worker(queue):
    queue.put('Merhaba Dünya!')

if __name__ == '__main__':
    queue=multiprocessing.Queue()
    processes=multiprocessing.Process(target=worker, args=(queue,))
    processes.start()
    print(queue.get())
    processes.join()