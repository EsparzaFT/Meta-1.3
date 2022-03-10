# Crear funcion para no repetir numeros, Fernando Esparza  Tinoco, 09/03/2022, 09/03/2022

def unNum(num):
    i = 0
    while i<5:
        j=input("Ingresa un numero: ")
        if not j in num:
            num.append(j)
            i= i+1
        else:
            print("Numero repetido, escribe de otro: ")

num = []
unNum(num)
print(num)
