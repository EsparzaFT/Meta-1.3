# Crear funcion que devuelva un diccionario con las veces que sale un numero Fernando Esparza  Tinoco, 09/03/2022, 09/03/2022

def frecuencias(lst):
    veces = []
    numero = []
    for f in range(len(lst)):
        contador = 0
        for n in lst:
            if lst[f] == n:
                contador += 1
                if (lst[f] in numero) == False:
                    numero.append(lst[f])
        veces.append(contador)
    diccionario = dict(zip(numero, veces))
    print(diccionario)

lst = [1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1]
frecuencias(lst)