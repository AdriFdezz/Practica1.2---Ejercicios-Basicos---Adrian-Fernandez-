#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo 
#es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa 
#que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono 
#sin el prefijo y la extensión.

def obtener_numero(telefono):
    partes = telefono.split('-')
    
    if len(partes) == 3 and partes[0] == "+34" and len(partes[1]) == 9 and len(partes[2]) == 2:
        numero_principal = partes[1]
        return numero_principal
    else:
        return "El número de teléfono no tiene el formato correcto."

if __name__ == "__main__":
    telefono = input("Introduce un número de teléfono con el formato +34-XXXXXXXXX-XX: ")
    numero_principal = obtener_numero(telefono)
    print(numero_principal)
