__author__ = 'Dean Bailey'
__author__ = 'abelamadou'

from threading import Thread
from random import choice, randint
from time import sleep

class Producer(Thread):
    '''
    This class is used to generate all the producer threads. Each thread will receive the dictionary of items that has the
    synchronized Queues in it to produce a random item and put them in the queues relative to the keys. The producer threads
    will randomly select an item/key from the dictionary and try to produce to its relative queue. If the queue isnt full they produce
    an item to it. If they succeed they sleep for a random time between 0-5 seconds. If the buffer size specified by the
    user is greater then 15 and all of the queues inside the dictionary of items are full then each producer will sleep for 15 seconds.
    '''
    def __init__(self,dictionary,name):
        Thread.__init__(self,name=name)
        self.dictionary_food = dictionary

    def run(self):
        while True:
            ingredient = choice(self.dictionary_food.keys())
            # lock.acquire()
            # print dictionary_food
            # print "Ingredient choice:",ingredient
            # lock.release()
            if self.dictionary_food[ingredient].qsize() != self.dictionary_food[ingredient].maxsize:
                self.dictionary_food[ingredient].put(str(self.name+"*"+ingredient))
                sleep(randint(0, 5))

            if self.dictionary_food[ingredient].maxsize > 15:
                full = True
                for i in self.dictionary_food.values():
                    if i.qsize() != self.dictionary_food[ingredient].maxsize:
                        full = False
                if full:
                    sleep(15)

