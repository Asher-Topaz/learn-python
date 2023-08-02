import math
import os
import random
import re
import sys

n = int(input("Enter a number: "))

if (n % 2) == 0:
    if 2 <= n <= 5:
        print('Not Weird')
    if 6 <= n <= 20:
        print('Weird')
    if n > 20:
        print('Not Weird')

elif (n % 2) != 0:
    print('Weird')


