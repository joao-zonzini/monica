#!/usr/bin/python3
# moeda.py 
# descrip
# jaz 01/21/22

import random

def bin_aleatorio():
    numero = int(random.random() * 10)
    return int(numero % 2 == 0)


for i in range(16):
    print("Jogada", i+1, "-", end=" ")
    for j in range(4):
        if (bin_aleatorio()) == 0:
            print("c", end="")
        else:
            print("x", end="")
    print("")

