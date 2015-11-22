__author__ = 'Dean'
import math

while True:
    z = input("z: ")
    R = input("R: ")
    y = input("y: ")
    x = input("x: ")

    print "lat: " + str(math.asin(z / R))
    print "lon: " + str(math.atan(y, x))



def from_c_t_c1_back(**c_t_c_set):

    z = c_t_c_set.get("z")
    R = c_t_c_set.get("R")
    y = c_t_c_set.get("y")
    x = c_t_c_set.get("x")

    print "lat: " + str(math.asin(z / R))
    print "lon: " + str(math.atan(y, x))

from_c_t_c1_back(z=4,R=9,y=8,x=8)