#create a factorial
from math import factorial


def get_factorial(num):
    num = 1
    
    for i in range(num):
     num *= i+1
     return num
    

    

    