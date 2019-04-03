import time
import os
import multiprocessing import Process, current_process

def square(numero):
    return numero * numero


def test():
    for i in range(1, 100000000):
        square(i)


if __name__ == '__main__':
    start = time.time()

    test()

    end = time.time()
    print(end - start)