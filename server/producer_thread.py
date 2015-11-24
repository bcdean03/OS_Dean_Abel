__author__ = 'Dean, Abel'
from threading import Thread
# from Queue import Queue
# from time import sleep
#
# q = Queue()
class Producer(Thread):
    def run(self):
        # while q.qsize() != 0:
            print str(q.get()) + " " + self.name


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
