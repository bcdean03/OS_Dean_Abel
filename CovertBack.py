__author__ = 'Dean'
import math

while True:
    z = input("z: ")
    R = input("R: ")
    y = input("y: ")
    x = input("x: ")

    print "lat: " + str(math.asin(z / R))
    print "lon: " + str(math.atan(y, x))