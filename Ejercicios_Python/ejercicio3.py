def operaciones():
    ancho = 17
    alto = 12

    resultado1 = ancho / 2
    resultado2 = ancho // 2
    resultado3 = alto / 3
    resultado4 = 1 + 2 * 5

    return "Operacion 1: " + str(resultado1) + "\nOperacion 2: " + str(resultado2) + "\nOperacion 3: " + str(resultado3) + "\nOperacion 4: " + str(resultado4)

if __name__ == "__main__":
    print(operaciones())