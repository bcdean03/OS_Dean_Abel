__author__ = 'Dean, Abel'
from threading import Thread


class Producer(Thread):
    def run(self):
        print "hello",self.namef
