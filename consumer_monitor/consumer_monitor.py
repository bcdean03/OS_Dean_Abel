__author__ = 'Dean, Abel'
import socket
from random import choice
from threading import *
from time import sleep

lock = RLock()


def main():
    # consumer_num = raw_input("How many consumers do you want?")
    # producer_num = raw_input("How many producers do you want to produce?")
    # buffer_size = raw_input("What is the size of the buffer you want to restrict the producers to produce?")
    consumer_num = 2000
    producer_num = 10
    buffer_size = 10

    s = socket.socket()
    s.connect(("192.168.1.141",5002))#request a connection with the listening server
    list= "%s %s"%(producer_num,buffer_size)
    s.send(list)
    data = s.recv(1024)
    if data != "Ready...":
        print "Error happened"
    s.close()
    return consumer_num


def client_socket(x,c_n):
    '''

    :param x: client name changing
    :param c_n: client name
    :return:
    '''
    buffer_server = ("192.168.1.141",5007)
    str_list = str(x)

    s = socket.socket()
    s.connect(buffer_server)#request a connection with the listening server
    # print c_n,"Connected to:->",buffer_server
    # print c_n,"Sending:->",str_list
    s.send(str_list)
    received = s.recv(1024)
    if not received:
        # print c_n, "Stopped receiving....."
        pass
    else:
        print  c_n,"Sending:->'Done'"
        s.send("Done")
        lock.acquire()
        print received
        lock.release()
        # print c_n,"Received:->",received
    s.close()


def create_recipe_dictionary():
    goodies_dictionary = {"Banana Bread": ["Banana", "Bread"],
                          "Apple Bread": ["Apple", "Bread"]}
    return goodies_dictionary


def get_food_and_recipe(goodies):
    food = choice(goodies.keys())
    recipe_list = goodies[food]
    return food, recipe_list


def consumers(consumer_num):
    food, recipe = get_food_and_recipe(create_recipe_dictionary())

    x = 0
    for i in xrange(int(consumer_num)):
        # Thread(target=client_socket, args=(x,"Client_{}".format(x))).start()
        Thread(target=client_socket, args=(x,"Client_{}".format(x))).start()
        sleep(.01)
        x += 1

if __name__ == '__main__':
    consumers(main())

    # consumers(10)

    # food, recipe = get_food_and_recipe(create_recipe_dictionary())
    # print food
    # print recipe
