#Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
#la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

def conversor_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == "__main__":
    celsius = int(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = conversor_fahrenheit(celsius)
    print(str(celsius) + " grados Celsius equivalen a " , int(fahrenheit) , " grados Fahrenheit.")
