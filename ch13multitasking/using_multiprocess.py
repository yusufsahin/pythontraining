import multiprocessing
#multiprocessing modülü, süreçler ile çoklu görev yapmayı sağlar
# ve iş parçacıklarının sınırlamalarını aşar.
def worker(num):
    print(f"Worker: {num}")


if __name__ == "__main__":
    processes=[]

    for i in range(5):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
