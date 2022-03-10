# Crear funcion que mueva la lista a la derecha, Fernando Esparza  Tinoco, 09/03/2022, 09/03/2022

def mueve_derecha(lst):
    voltear = len(lst)
    operacion = voltear-1
    lst = lst[operacion:] + lst[:operacion]
    print(lst)

lst = [2, 4, 6, 8, 10]

mueve_derecha(lst)