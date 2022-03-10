# Crear funcion que devuelva positivos y negativos, Fernando Esparza  Tinoco, 09/03/2022, 09/03/2022

numeros = [69, -37, 0, -27, -59, 83, 1, 45]

def PositNegat(lst):

    lst.sort()
    positivos = []
    negativos = []
    for i in lst:
        if i >= 0:
            positivos.append(i)
        else:
            negativos.append(i)
    return positivos, negativos

positivos, negativos = PositNegat(numeros)
print(positivos, negativos)