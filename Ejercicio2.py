# Contar Mayusculas y minisculas, Fernando Esparza  Tinoco, 09/03/2022, 09/03/2022

def contar (n):
    contador = {'Minus' : 0, 'Mayor' : 0}
    for i in n:
        if i.islower():
            contador ['Minus'] += 1
        else:
            if i.isupper():
                contador ['Mayor'] += 1
    return  contador

print(contar(input("Ingresa una palabra")))