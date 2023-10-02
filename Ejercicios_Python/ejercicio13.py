#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: 
#"la división de n entre m da un cociente c y un resto r", donde n y m son 
#los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

def division(n, m):
    cociente = n // m
    resto = n % m
    return cociente, resto

if __name__ == "__main__":
    numero1 = int(input("Ingresa un número entero n: "))
    numero2 = int(input("Ingresa otro número entero m: "))
    cociente, resto = division(numero1, numero2)
    mensaje = "La división de " + str(numero1) + " entre " + str(numero2) + " da un cociente " + str(cociente) + " y un resto " + str(resto)
    print(mensaje)

