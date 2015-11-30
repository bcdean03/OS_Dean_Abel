__author__ = 'Dean Bailey abelamadou'
import socket
from producer_thread import *
from Queue import Queue
from threading import Thread,RLock
# global dictionary_food
from time import sleep
# self.dictionary_food={}
lock = RLock()


class ProducerServer:
    '''
    This class acts as a server for the ingredients produced by the producers.
    Each client will receive a thread for the socket and exchange infromation. The server
    will serve the client and the server will receive requests from the client. The producers
    will randomly generate items to the dictionary_food queues inside of it.
    '''
    dictionary_food={}
    def user_main_socket(self):
        '''
        This method creates a socket and listens for a connection from the main user. This method receives
        the buffer size and the amount of producers to produce into their respective items queue. This listens on a different
        port then the sockets created below.
        :return: N/A
        '''
        # addr= ("192.168.1.141", 5002)
        # addr= ("192.168.1.193", 5002)
        addr= ("10.10.112.136", 5002)
        # addr= ("10.136.139.204", 5002)
        sock = socket.socket()
        sock.bind(addr)
        sock.listen(1)
        print "Waiting for connection first user..."
        client,client_addr = sock.accept()
        print "Made connection with client --->",client_addr
        user_info_in = client.recv(1024)
        # user_info_list = convert_input_to_list(user_info_in)
        user_info_list = user_info_in.split(' ')
        self.setup_all(user_info_list)
        print "!!!Going to send Ready!!!"
        client.send("Ready...")
        "Closing socket..."
        sock.close()
        self.start_listening()


    def setup_bf(self,bf_size):
        '''
        This method creates a synchronized Queue for each ingredient in the list to the dictionary and sets the size of them
        as the number passed in from the main user.
        :param bf_size: This is the size of the buffer passed in from set up all.
        :return:
        '''
        list = ["Apple", "Banana", "Bread", "Salt", "Flour", "Cinnamon", "Pepperoni", "Oil",
                "Eggs", "Sugar", "Raisin", "Baking Soda", "Butter", "Yeast", "Water",
                "Pumpkin", "Wheat Flour", "Honey", "Chocolate Chips",
                "Milk", "Noodles", "Hamburger", "Lettuce", "Cheese", "Sauce"]
        # global self.dictionary_food

        for i in list:
            self.dictionary_food[i]= Queue(maxsize=bf_size)


    def start_listening(self):
        '''
        This method starts listening for the clients who want to get items from the Abean grocery store. This
        socket is listening on another port, not the one the first user used. It accepts up 1000 clients at a time,
        but we are limited due to our computers limitations. Exceptions have been caught. This creates a client threaded socket
        every time it receives another connection
        :return:
        '''
        # addr= ("192.168.1.141", 5007)
        # addr= ("192.168.1.193", 5007)
        addr= ("10.10.112.136", 5007)
        # addr= ("10.136.139.204", 5007)
        sock = socket.socket()
        sock.bind(addr)
        sock.listen(1000)
        count = 0
        while True:
            print "Waiting for connection from clients..."
            client, client_addr = sock.accept()
            try:
                Thread(target=self.client_threaded_socket, args=(client,)).start()
                sleep(.1)
                count+=1
            except Exception as e:
                print "Too many producers and clients. Lower the amount of producers"
                print "Continuing with this amount of clients:",(count+1)
                break
        sock.close()



    def client_threaded_socket(self,client):
        '''
        This method is a thread that runs the connection between the client and the server. This receives an ingredient
        from the client and then attempts to get the item out of the dictionary where the items are being stored in queues
        which are values for each key. If the queue is empty then the thread will wait until a producer has put an item in that queue.
        When the thread has taken the item out of the queue, then it will send it back to the client. This will continue until the client
        tells the server its completed its list of items for the food they want to create by sending "Done". The queues take care of synchronization.
        :param client:
        :return:
        '''
        try:
            ingredient_item = client.recv(1024)
            while ingredient_item!="Done":
                lock.acquire()
                print">>>> Requested ingredient:->",ingredient_item
                lock.release()
                print "ingredient item:",ingredient_item
                p_ingredient_item = self.dictionary_food[ingredient_item].get()
                lock.acquire()
                print"<<<< Sending ingredient:->",p_ingredient_item
                lock.release()
                client.send(p_ingredient_item)

                ingredient_item = client.recv(1024)
        except socket.error as error:
            print "{"+error+"}","Wasn't able to send 'Done' because lost connection"
        finally:
            print "Closing client_socket..."
            client.close()

    def setup_all(self,user_info):
        '''
        This method sets up all the producers threads that the main user specified. It calls set_up_bf that
        sets up the dictionary that holds all the items that will be produced by the producers. They all receive
        names so later in the gui we can figure out which producer produced the item that the client received.
        Exceptions are caught.
        :param user_info:
        :return:
        '''
        if len(user_info) == 2:
            num_producers = int(user_info[0])
            self.setup_bf(int(user_info[1]))
            print "MAKING",num_producers,"PRODUCERS!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            if num_producers > 500:
                print "Too many producers, System cant handle."
                print "Exiting... Try again."
                exit(0)
            else:
                for i in xrange(0, num_producers):
                    try:
                        Producer(self.dictionary_food,"Producer_{}:".format(i+1)).start()
                        # Producer(self.dictionary_food,"Producer_{}".format(i+1)).start()
                    except Exception as e:
                        print "Exception:",e
                        print "Cant handle that many producers... Too poor to pay them all!"
                        print "Not enough resources told consumers and producers. Lower producers!"
                        print "Exit!!!!!!!!!!!!"
                        exit(0)
        else:
            print("System exit... Incorrect data")
            exit(0)
        print "PRODUCERS ARE DONE"

if __name__ == '__main__':

    ProducerServer().user_main_socket()