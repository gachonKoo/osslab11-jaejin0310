import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def calculate_circle_area(r):
    return math.pi * r**2

import geo.utils as utils

a,b=3,4
c=utils.calculate_hypotenuse(a, b)
print('c=',c)

r=10
area=utils.calculate_circle_area(r) 
print('area=',area)
