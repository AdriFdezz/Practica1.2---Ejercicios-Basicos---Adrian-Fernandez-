#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y 
#muestre por pantalla cada uno de los productos en una línea distinta.

def cesta_compra(productos):
    lista_productos = productos.split(',')
    return lista_productos

if __name__ == "__main__":
    productos = input("Escribe los productos separados por comas: ")
    lista = cesta_compra(productos)
    for producto in lista:
        print(producto.strip())
