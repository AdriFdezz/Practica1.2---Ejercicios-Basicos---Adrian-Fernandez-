#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre 
#por pantalla la misma frase pero con la vocal introducida en mayúscula.

def cambiar_vocal(frase, vocal):
    return (frase.replace(vocal, vocal.upper()))

if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    vocal = input("Escribe una vocal: ")
    if vocal in 'aeiou':
        print(cambiar_vocal(frase,vocal))
    else:
        print("Intentalo otra vez")