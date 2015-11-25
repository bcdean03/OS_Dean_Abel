__author__ = 'Dean, Abel'
from threading import Thread
# from Queue import Queue
# from producer_server import *
from random import choice, randint
from time import sleep


# from time import sleep
# q = Queue()


class Producer(Thread):
    def __init__(self,dictionary,name):
        Thread.__init__(self,name=name)
        self.dictionary_food = dictionary

    def run(self):
        while True:
            # global dictionary_food
            ingredient = choice(["Bread", "Apple", "Banana"])
            # print "INGREEEEEEEEEEEEEEEEEEEEEEEDIENT:", ingredient
            # lock.acquire()

            # print dictionary_food
            # print "Ingredient choice:",ingredient

            # lock.release()
            if self.dictionary_food[ingredient].qsize() != self.dictionary_food[ingredient].maxsize:
                print"STILLL GOING FUCK YOU GUYS"
                self.dictionary_food[ingredient].put(str(self.name+": "+ingredient))
            elif self.dictionary_food[ingredient].qsize() == self.dictionary_food[ingredient].maxsize:
                print"STILLL GOING FUCK YOU GUYS"
                sleep(randint(0,5))

            # self.dictionary_food[ingredient].put(ingredient)

            # dictionary_food[choice(["Bread", "Apple", "Banana"])].put()
            # sleep(2)
            # sleep(randint(0,5))


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
