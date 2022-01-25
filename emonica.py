#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print("Faltou numero de jogadas. Terminando o programa.")
    exit(0)

import random
import numpy as np
import matplotlib.pyplot as plt
import utils.bairro as bairro
import utils.amigos as amigos

n_jogadas = int(sys.argv[1])
n_movimentos = 4

def bin_aleatorio():
    numero = int(random.random() * 10)   ## numero menor do que 1 se torna maior do que 1
    return int(numero % 2 == 0)     ## retorna 0 ou 1 dependendo se o numero eh par ou impar


for i in range(n_jogadas):
    monica_yx = [4, 0]
    for j in range(n_movimentos):
        if (bin_aleatorio()):
            monica_yx[0] = monica_yx[0] - 1

    visitado = amigos.amigo_visitado(monica_yx)


for i in amigos.dict_amigo:
    print(f"{i} foi visitado {amigos.dict_amigo[i]} / {n_jogadas} --> {(amigos.dict_amigo[i]/n_jogadas)*100}%")

nomes = list(amigos.dict_amigo.keys())
valores = list(amigos.dict_amigo.values())

for i in range(len(valores)):
    valores[i] = (valores[i] / n_jogadas) * 100

y_pos = np.arange(4)
plt.bar(range(len(amigos.dict_amigo)), valores, tick_label=nomes)

for index, value in enumerate(valores):
    plt.text(value, index, str(value), color='black')

plt.show()
