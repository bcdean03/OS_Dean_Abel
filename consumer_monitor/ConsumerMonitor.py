__author__ = 'Dean, Abel'
import socket

def main():
    consumer_num = raw_input("How many consumers do you want?")
    producer_num = raw_input("How many producers do you want to produce?")
    buffer_size = raw_input("What is the size of the buffer you want to restrict the producers to produce?")
    s = socket.socket()
    s.connect(("localhost",5002))#request a connection with the listening server
    s.send(consumer_num,producer_num,buffer_size)
    data = s.recv(1024)
    if data != "received":
        print "Error happened"
    s.close()

if __name__ == '__main__':
    main()
