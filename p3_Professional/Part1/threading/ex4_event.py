import threading
import time

# пример событий

def producer():
    time.sleep(10)
    print('Producer found!')
    product.set()
    product.clear()


def consumer():
    print('product wait')
    product.wait()
    print('Product exist')


product = threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

task1.join()
task2.join()
