# Crear funcion quedevuelva el valor medio de una matriz, Fernando Esparza  Tinoco, 09/03/2022, 09/03/2022

def media_filas(lst):
    suma = 0
    media = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            suma += lst[i][j]
        media.append(suma / (j + 1))
        suma = 0
    print(media)
lst = [[1,2,3,4], [1,3,5,7]]
media_filas(lst)