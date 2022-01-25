#!/usr/bin/python3
# amigos.py
# descrip
# jaz 01/22/22

dict_amigo = {
    "Horácio": 0,
    "Cebolinha": 0,
    "Magali": 0,
    "Cascao": 0,
    "Bidu": 0
}

def amigo_visitado(monica_yx):
    if monica_yx[0] == 0:
        visitado = "Horácio"
    elif monica_yx[0] == 1:
        visitado = "Cebolinha"
    elif monica_yx[0] == 2:
        visitado = "Magali"
    elif monica_yx[0] == 3:
        visitado = "Cascao"
    else:
        visitado = "Bidu"

    dict_amigo[visitado] +=1
    return visitado
