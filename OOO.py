__author__ = 'DeanBailey and AbelAmadou'
print("Got you good you fugger")
from time import sleep
from time import clock
from Queue import Queue
from threading import Thread
q = Queue(maxsize=10)


def driver():
    while True:
        clock_time = clock()
        while clock() < clock_time+5:
            print("size:", str(q._qsize()), q.get().hello_world())
            sleep(.01)
        sleep(10)


class HelloWorld:
    def __init__(self, i):
        self.i = i

    def hello_world(self):
        return "Hello World " + str(self.i)


def put_into_queue(h):
    q.put(h)

thrd_driver = Thread(target=driver)
thrd_driver.start()
i = 0

while True:
    hello = HelloWorld(i)
    Thread(target=put_into_queue, args=(hello,)).start()
    i += 1
    sleep(.09)


# clock_time = clock()
# print clock_time
# print((clock_time+5))
