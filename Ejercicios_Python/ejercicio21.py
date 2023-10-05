#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla 
#la frase invertida.

def invertir_frase(frase):
    frase_invertida = frase[::-1]
    return frase_invertida

if __name__ == "__main__":
    frase = input("Escribe una frase para invertirla: ")
    frase_invertida = invertir_frase(frase)
    print("Frase invertida: " + frase_invertida)


