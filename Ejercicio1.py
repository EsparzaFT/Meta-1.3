# Funcion de string que devuelve sin numeros, Fernando Esparza  Tinoco, 02/03/2022, 09/03/2022


import re

string = input("Ingrese campo")

def borrar_numeros (string):
    borrarNum = re.sub(r'[0-9]+', '', string)
    print(borrarNum)

borrar_numeros(string)