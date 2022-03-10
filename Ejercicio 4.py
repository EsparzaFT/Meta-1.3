# Crear funcion para desencriptar mensaje, Fernando Esparza  Tinoco, 09/03/2022, 09/03/2022

def encripta(s,clave):
    letras = "abcdefghijklmnopqrstuvwxyz"
    desencriptar = s
    cifrado = ""

    for f in range(len(s)):
        for n in range(len(clave)):
            if s[f] == desencriptar[f]:
                desencriptar = s.replace(clave[n], letras[n])
        cifrado += desencriptar[f]

        print("Mensaje encriptado: ", cifrado)

clave = "ixmrklstnuzbowfaqejdcpvhyg"
s = input("Ingresa un mensaje: ")
encripta(s,clave)
