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
            ingredient = choice(self.dictionary_food.keys())
            # print "INGREEEEEEEEEEEEEEEEEEEEEEEDIENT:", ingredient
            # lock.acquire()

            # print dictionary_food
            # print "Ingredient choice:",ingredient

            # lock.release()
            if self.dictionary_food[ingredient].qsize() != self.dictionary_food[ingredient].maxsize:
                self.dictionary_food[ingredient].put(str(self.name+": "+ingredient))
                sleep(randint(0,5))

            if self.dictionary_food[ingredient].maxsize > 15:
                full = True
                for i in self.dictionary_food.values():
                    if i.qsize != self.dictionary_food[ingredient].maxsize:
                        full = False
                if full:
                    print self.name+": Sleeping for 15 seconds."
                    sleep(15)


            # elif self.dictionary_food[ingredient].qsize() == self.dictionary_food[ingredient].maxsize:
            #     sleep(randint(0,5))
            # print ingredient
            # print self.name,":->",ingredient
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
