import math

def calculate_hypotenuse(a, b):
    """피타고라스 정리로 빗변 계산"""
    return math.sqrt(a**2 + b**2)

def calculate_circle_area(r):
    """원의 면적 계산"""
    return math.pi * r**2

import geo.utils as utils

a,b=3,4
c=utils.calculate_hypotenuse(a, b)
print('c=',c)

r=10
area=utils.calculate_circle_area(r) 
print('area=',area)
