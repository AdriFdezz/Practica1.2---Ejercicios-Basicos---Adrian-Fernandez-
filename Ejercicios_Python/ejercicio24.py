#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre ~
#por pantalla el número de euros y el número de céntimos del precio introducido.

def euros_y_centimos(precio):
    euros = int(precio)
    centimos = int((precio - euros) * 100)
    return euros, centimos

if __name__ == "__main__":
    precio = float(input("Introduce el precio con dos decimales: "))
    euros, centimos = euros_y_centimos(precio)
    print("El precio es de " + str(euros) + " euros y " + str(centimos) + " céntimos.")
