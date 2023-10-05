#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra 
#por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando 
#el día o el mes se introduzcan con un solo carácter.

def fecha_nacimiento(dia, mes, year):
    return "Día: " + dia + ", Mes: " + mes + ", Año: " + year

if __name__ == "__main__":
    fecha = input("Escribe tu fecha de nacimiento en el siguiente formato dd/mm/aaaa: ")

    partes = fecha.split("/")
    
    if len(partes) != 3:
        print("Formato incorrecto. Debe ser dd/mm/aaaa")
    else:
        dia = partes[0]
        mes = partes[1]
        year = partes[2]
        resultado = fecha_nacimiento(dia, mes, year)
        print(resultado)
