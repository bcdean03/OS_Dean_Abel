__author__ = 'Dean, Abel'
import socket
from Producer import Producer


def user_main():
    try:
        addr= ("192.168.1.141", 5002)
        sock = socket.socket()
        sock.bind(addr)
        sock.listen(1)
        print "Waiting for connection..."
        client,client_addr = sock.accept()
        print "Made connection with client --->",client_addr
        user_info_in = client.recv(1024)
        print "Received:", user_info_in
        user_info_list = user_info_in.split(' ')
        print user_info_list
        client.send("received")
    finally:
        "Closing socket..."
        sock.close()
        client.close()
        return user_info_list


def setup(user_info):
    if len(user_info) == 2:
        num_producers = int(user_info[0])
        buffer_size = int(user_info[1])
        for i in xrange(0, num_producers):
            Producer(name="Producer_{}".format(i+1)).start()
            # print(i)
    else:
        print("System exit... Incorrect data")
        exit(0)

if __name__ == '__main__':
    setup(user_main())
    # setup([10, 10])
    # setup([10, 10, 1])




