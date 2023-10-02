#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
#así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
#Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas 
#vendidos en el último pedido y calcule el peso total del paquete que será enviado.

def calcular_peso(payasos, munecas):
    peso_payasos = payasos * 112
    peso_munecas = munecas * 75
    peso_total = peso_payasos + peso_munecas
    return peso_total

if __name__ == "__main__":
    payasos = int(input("Ingresa la cantidad de payasos vendidos: "))
    munecas = int(input("Ingresa la cantidad de muñecas vendidas: "))
    peso_total = calcular_peso(payasos, munecas)
    mensaje = "El peso total del paquete a enviar es de " + str(peso_total) + " gramos."
    print(mensaje)
