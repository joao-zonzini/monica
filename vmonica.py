#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print("Faltou numero de jogadas. Terminando o programa.")
    exit(0)

import random
import utils.bairro as bairro
import utils.amigos as amigos

n_jogadas = int(sys.argv[1])
n_movimentos = 4

def bin_aleatorio():
    numero = int(random.random() * 10)   ## numero menor do que 1 se torna maior do que 1
    return int(numero % 2 == 0)     ## retorna 0 ou 1 dependendo se o numero eh par ou impar


for i in range(n_jogadas):
    print("--- JOGADA", i+1, "---")
    mapa_bairro = bairro.reseta_bairro()
    bairro.printar_bairro(mapa_bairro)
    monica_yx = [4, 0]
    trajetoria = ""
    for j in range(n_movimentos):
        mapa_bairro[monica_yx[0]][monica_yx[1]] = "o"
        if (bin_aleatorio()):
            trajetoria += "c"
            monica_yx[0] = monica_yx[0] - 1
        else:
            trajetoria += "x"
            monica_yx[1] = monica_yx[1] + 1

        mapa_bairro[monica_yx[0]][monica_yx[1]] = "x"
        bairro.printar_bairro(mapa_bairro)


    visitado = amigos.amigo_visitado(monica_yx)
    print(trajetoria, " --> ", visitado, sep="")

print("----------")
for i in amigos.dict_amigo:
    #print(i, "foi visitado", amigos.dict_amigo[i], "de", n_jogadas, "vezes. -->", (amigos.dict_amigo[i]/n_jogadas)*100, "%")
    print(f"{i} foi visitado {amigos.dict_amigo[i]} de {n_jogadas} vezes --> {(amigos.dict_amigo[i]/n_jogadas)*100}%")
