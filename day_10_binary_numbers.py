
import math
import os
import random
import re
import sys

def deci(number):
    myCount = 0
    maxim = 0
    while number > 0:
        if number%2 == 1:
            myCount = myCount + 1
            if myCount > maxim:
                maxim = myCount
        else:
            myCount = 0
        number = number//2
    print(maxim)

if __name__ == '__main__':
    n = int(input())
    deci(n)
