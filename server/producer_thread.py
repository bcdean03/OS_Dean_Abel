__author__ = 'Dean, Abel'
from threading import Thread
from Queue import Queue
from producer_server import *
from random import choice, randint
from time import sleep

# from time import sleep
q = Queue()


class Producer(Thread):
    def run(self):
        while True:
            ingredient = choice(["Bread", "Apple", "Banana"])
            dictionary_food[ingredient].put(self.name+": "+ingredient)
            # dictionary_food[choice(["Bread", "Apple", "Banana"])].put()
            sleep(randint(0,5))
        # print self.name
        # while q.qsize() != 0:
        #     print str(q.get()) + " " + self.name


# def wait_to_put():
#     q.put(1)
#
#
# if __name__ == '__main__':
#     for i in range(0,30):
#         Producer(name="{}".format(i+1)).start()
#     sleep(2)
#     wait_to_put()
#     wait_to_put()
#     wait_to_put()
#     wait_to_put()
#     wait_to_put()
#     wait_to_put()
#     wait_to_put()
#     wait_to_put()
#
