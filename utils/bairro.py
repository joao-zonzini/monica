#!/usr/bin/python3
# bairro.py
# descrip
# jaz 01/22/22

def reseta_bairro():
    bairro = [["h", "o", "o", "o", "o"],
    ["o", "c", "o", "o", "o"],
    ["o", "o", "m", "o", "o"],
    ["o", "o", "o", "a", "o"],
    ["x", "o", "o", "o", "b"]]

    return bairro


def printar_bairro(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            print(mapa[i][j], end="")
        print("")
    print("")
