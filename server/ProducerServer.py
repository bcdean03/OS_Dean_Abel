__author__ = 'Dean, Abel'
import socket


def main():
    try:
        addr= ("192.168.1.141", 5002)
        sock = socket.socket()
        sock.bind(addr)
        sock.listen(1)
        print "Waiting for connection..."
        client,client_addr = sock.accept()
        print "Made connection with client --->",client_addr
        list_in = client.recv(1024)
        print "Received:", list_in
        client.send("received")
    finally:
        "Closing socket..."
        sock.close()
        client.close()



if __name__ == '__main__':
    main()


