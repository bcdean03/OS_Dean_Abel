__author__ = 'Dean, Abel'
import socket
from producer_thread import *
from Queue import Queue
from threading import Thread,RLock
global dictionary_food
from time import sleep
dictionary_food={}
lock = RLock()



def user_main_socket():
    # addr= ("192.168.1.141", 5002)
    addr= ("192.168.1.136", 5002)
    sock = socket.socket()
    sock.bind(addr)
    sock.listen(1)
    print "Waiting for connection first user..."
    client,client_addr = sock.accept()
    print "Made connection with client --->",client_addr
    user_info_in = client.recv(1024)
    # print "Received:", user_info_in
    user_info_list = convert_input_to_list(user_info_in)
    # user_info_list = user_info_in.split(' ')
    setup_all(user_info_list)
    print "!!!Going to send Ready!!!"
    client.send("Ready...")
    "Closing socket..."
    sock.close()
    # client.close()
    # return user_info_list
    start_listening()


def setup_bf(bf_size):
    list = ["Apple", "Banana", "Bread", "Salt", "Flour", "Cinnamon", "Pepperoni", "Oil",
            "Eggs", "Sugar", "Raisin", "Baking Soda", "Butter", "Yeast", "Water",
            "Banana", "Apple", "Pumpkin", "Wheat Flour", "Honey", "Chocolate Chips",
            "Milk", "Noodles", "Hamburger", "Lettuce", "Cheese", "Hamburger", "Sauce"]
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
    # addr= ("192.168.1.141", 5007)
    addr= ("192.168.1.136", 5007)
    sock = socket.socket()
    sock.bind(addr)
    sock.listen(1000)
    count = 0
    while True:
        print "Waiting for connection from clients..."
        client, client_addr = sock.accept()
        # print "Made connection with client --->",client_addr
        # ingredient_item = client.recv(1024) #Going to receive some byte from the connection with max byte of 1024
        # Thread(target=client_threaded_socket, args=(client, client_addr, ingredient_item)).start()
        try:
            Thread(target=client_threaded_socket, args=(client, client_addr)).start()
            sleep(.1)
            count+=1
        except Exception as e:
            print "Too many producers and clients. Lower the amount of producers"
            print "Continuing with this amount of clients:",(count+1)
            break
    sock.close()



def client_threaded_socket(client, client_address):
    # print "Made connection with client --->",client_address
    # str = " ".join(ingredient_list)
    # print "Sending:",str
    try:
        ingredient_item = client.recv(1024)
        while ingredient_item!="Done":
            # ingredient_item = client.recv(1024)
            lock.acquire()
            print">>>> Requested item picture:->",ingredient_item
            # picture = getPicture()
            # print "Sending:->",picture
            lock.release()
            p_ingredient_item = dictionary_food[ingredient_item].get()
            lock.acquire()
            print"<<<< Sending picture:->",p_ingredient_item
            lock.release()
            client.send(p_ingredient_item)

            ingredient_item = client.recv(1024)
            # if not test:
            # client.close()
            # if test=="Done":
            #     print "Closing client_socket.........."
            #     client.close()
        # if not ingredient_item:
        #     print "!!!!!!Socket must be already closed, since not receiving anything anymore!!!!!!"
        # else:
        #     print "Closing client_socket.........."
        #     client.close()
    except socket.error as error:
        print "{"+error+"}","Wasn't able to send 'Done' because lost connection"
    finally:
        print "Closing client_socket..."
        client.close()


        # for synchronization and removing from the list later implementation.... TODO
        # for i in ingredient_list:

        #the information we send back is the pictures of the food to make banana bread
        # print "Sending:", str(data),"to(",client.name+")"
        # client.send(data)

    # client.close()


def setup_all(user_info):
    if len(user_info) == 2:
        num_producers = int(user_info[0])
        setup_bf(int(user_info[1]))
        list_of_prods = []
        print "MAKING",num_producers,"PRODUCERS!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        if num_producers > 500:
            print "Too many producers, System cant handle."
            print "Exiting... Try again."
            exit(0)
        else:
            for i in xrange(0, num_producers):
                try:
                    Producer(dictionary_food,"Producer_{}".format(i+1)).start()
                    # sleep(.01)
                except Exception as e:
                    print "Exception:",e
                    print "Cant handle that many producers... Too poor to pay them all!"
                    print "Not enough resources told consumers and producers. Lower producers!"
                    print "Exit!!!!!!!!!!!!"
                    # raise SystemExit(0)
                    exit(0)
            # Producer(dictionary_food,name="Producer_{}".format(i+1)).start()
            # print(i)
    else:
        print("System exit... Incorrect data")
        exit(0)
    print "PRODUCERS ARE DONE"
    # return True

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
