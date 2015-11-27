__author__ = 'Dean, Abel'
from threading import Thread
from random import choice, randint
from time import sleep

class Producer(Thread):
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
                self.dictionary_food[ingredient].put(str(self.name+" "+ingredient))
                sleep(randint(0, 5))

            if self.dictionary_food[ingredient].maxsize > 15:
                full = True
                for i in self.dictionary_food.values():
                    if i.qsize() != self.dictionary_food[ingredient].maxsize:
                        full = False
                if full:
                    sleep(15)

