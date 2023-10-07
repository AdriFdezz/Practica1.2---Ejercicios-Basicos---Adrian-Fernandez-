#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre 
#por pantalla una cadena con el nombre del producto seguido de su precio unitario 
#con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total 
#con 8 dígitos enteros y 2 decimales.

def calcular_productos(nombre, precio, unidades):
    precio_formato = '{:.2f}'.format(precio)
    unidades_formato = '{:03d}'.format(unidades)
    coste_total = precio * unidades
    coste_total_formato = '{:.2f}'.format(coste_total)
    
    return f"Nombre del producto: {nombre}\nPrecio unitario: {precio_formato}\nNúmero de unidades: {unidades_formato}\nCoste total: {coste_total_formato}"

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio unitario del producto: "))
    unidades = int(input("Ingrese el número de unidades: "))
    print("")
    
    resultado = calcular_productos(nombre, precio, unidades)
    
    print(resultado)
