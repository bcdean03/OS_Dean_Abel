__author__ = 'Dean, Abel'
import socket


def main():

    addr =("192.168.1.141",5002)
    sock = socket.socket()
    sock.bind(addr)
    sock.listen(1)
    client,client_addr = sock.accept()
    print "Made connection with client --->",client_addr
    list_in = sock.recv(1024)
    print "Received:", list_in
    sock.send("received")
    sock.close()




if __name__ == '__main__':
    main()


