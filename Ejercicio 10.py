# Crear diccionario que guarde distintas temp. Fernando Esparza  Tinoco, 09/03/2022, 09/03/2022

dict = {'Londres': [3.4, 6.3, 10.5], 'Oslo': [-3.8, -5.0, 4.2], 'Rennes': [2.5, 3.1, 12.3]}

def mediaTemp(dict):
    valor = list(dict.values())
    medio = []
    for f in range(len(valor)):
        suma = 0
        for n in valor[f]:
            suma += n
        medio.append(suma/len(valor[f]))
    print(medio)

def minimasTemp(dict):
    resultado = {}
    for key in dict:
        minimo = min(dict[key])
        resultado[key]=minimo
    print(resultado)

def minTemp(dict):
    minimo = []
    boolean = True
    resultado = {}
    for key in dict:
        for n in (dict[key]):
            if boolean == True:
                tem = n
                boolean = False
            else:
                if n <= tem:
                    tem = n
                    resultado[key] = tem
    minimo.append(tem)
    print(resultado)

mediaTemp(dict)
minimasTemp(dict)
minTemp(dict)