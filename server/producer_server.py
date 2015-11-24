__author__ = 'Dean, Abel'
import socket
from producer_thread import Producer
from Queue import Queue
from threading import Thread
global dictionary_food
from time import sleep
dictionary_food={}



def user_main_socket():
    try:
        addr= ("192.168.1.141", 5002)
        sock = socket.socket()
        sock.bind(addr)
        sock.listen(1)
        print "Waiting for connection..."
        client,client_addr = sock.accept()
        print "Made connection with client --->",client_addr
        user_info_in = client.recv(1024)
        # print "Received:", user_info_in
        user_info_list = convert_input_to_list(user_info_in)
        # user_info_list = user_info_in.split(' ')
        setup_all(user_info_list)
        print "!!!Going to send Ready!!!"
        client.send("Ready...")
    finally:
        "Closing socket..."
        sock.close()
        # client.close()
        # return user_info_list
        start_listening()


def setup_bf(bf_size):
    list = ["apple","rice","banana"]
    global dictionary_food
    # print "1:",dictionary_food

    for i in list:
        # dictionary_food.update({i:Queue(maxsize=bf_size)})
        # a =Queue(maxsize=bf_size)
        # a.put(10)
        # dictionary_food[i]=a
        dictionary_food[i]= Queue(maxsize=bf_size)
    # start_listening()


def convert_input_to_list(input_string):
    return input_string.split(' ')


def start_listening():
    addr= ("192.168.1.141", 5007)
    sock = socket.socket()
    sock.bind(addr)
    sock.listen(100)
    while True:
        print "Waiting for connection..."
        client, client_addr = sock.accept()
        # print "Made connection with client --->",client_addr
        ingredient_list = convert_input_to_list(client.recv(1024))#Going to receive some byte from the connection with max byte of 1024
        Thread(target=client_threaded_socket, args=(client, client_addr, ingredient_list)).start()
    sock.close()



def client_threaded_socket(client, client_address, ingredient_list):
    # print "Made connection with client --->",client_address
    str = " ".join(ingredient_list)
    # print "Sending:",str
    client.send(str)
    test = client.recv(1024)
    # if not test:
    # client.close()
    if test=="Done":
        print "Closing client_socket.........."
        client.close()

        # for synchronization and removing from the list later implementation.... TODO
        # for i in ingredient_list:

        0

        #the information we send back is the pictures of the food to make banana bread
        # print "Sending:", str(data),"to(",client.name+")"
        # client.send(data)

    # client.close()


def setup_all(user_info):
    if len(user_info) == 2:
        num_producers = int(user_info[0])
        setup_bf(int(user_info[1]))
        for i in xrange(0, num_producers):
            Producer(name="Producer_{}".format(i+1)).start()
            # print(i)
    else:
        print("System exit... Incorrect data")
        exit(0)

if __name__ == '__main__':
    # global dictionary_food

    # setup(user_main_socket())
    user_main_socket()
    # setup([10, 10])
    # setup([10, 10, 1])
    # print "0:",dictionary_food
    # setup_bf(3)
    # print "3:",dictionary_food
    # print "len->",len(dictionary_food)
    # dictionary_food["apple"].put(5)
    # for i in dictionary_food.values():
    #     print i.maxsize
