import multiprocessing

def worker(queue, message):
    queue.put(message)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    messages = ['Merhaba Dünya!', 'Hello World!', 'Bonjour le monde!', 'Hola Mundo!']
    processes = []

    # Her mesaj için bir işlem oluştur ve başlat
    for message in messages:
        process = multiprocessing.Process(target=worker, args=(queue, message))
        processes.append(process)
        process.start()

    # Her işlemden mesajları al ve yazdır
    for _ in processes:
        print(queue.get())

    # Tüm işlemlerin tamamlanmasını bekle
    for process in processes:
        process.join()
