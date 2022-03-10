# Crear funcion para encriptar mensaje, Fernando Esparza  Tinoco, 09/03/2022, 09/03/2022

def encripta(s,clave):
    letras = "abcdefghijklmnopqrstuvwxyz"
    encriptar = s
    cifrado = ""

    for f in range(len(s)):
        for n in range(len(clave)):
            if s[f] == encriptar[f]:
                encriptar = s.replace(letras[n], clave[n])
        cifrado += encriptar[f]

        print("Mensaje encriptado: ", cifrado)

clave = "ixmrklstnuzbowfaqejdcpvhyg"
s = input("Ingresa un mensaje: ")
encripta(s,clave)
