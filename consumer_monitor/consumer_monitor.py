__author__ = 'Dean, Abel'
import socket
from random import randint
from threading import Thread
from time import sleep
def main():
    consumer_num = raw_input("How many consumers do you want?")
    producer_num = raw_input("How many producers do you want to produce?")
    buffer_size = raw_input("What is the size of the buffer you want to restrict the producers to produce?")
    s = socket.socket()
    s.connect(("192.168.1.141",5002))#request a connection with the listening server
    list= "%s %s"%(producer_num,buffer_size)
    s.send(list)
    data = s.recv(1024)
    if data != "Ready...":
        print "Error happened"
    s.close()
    return consumer_num


def client_socket():
    buffer_server = ("192.168.1.141",5007)
    str_list = str(randint(0,10))
    s = socket.socket()
    s.connect(buffer_server)#request a connection with the listening server
    print Thread.name,"Connected to:->",buffer_server
    print Thread.name,"Sending:->",str_list
    s.send(str_list)
    received = s.recv(1024)
    if not received:
        print "*"*40
    else:
        print Thread.name,"Received:->",received
    # s.send("Done")
    # sleep(1)
        s.close()

def consumers(consumer_num):
    x = 0
    for i in xrange(int(consumer_num)):
        Thread(target=client_socket, name="Client_{}".format(x)).start()
        x += 1


if __name__ == '__main__':
    consumers(main())
    # consumers(10)