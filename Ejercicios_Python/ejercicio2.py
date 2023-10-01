#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

def importe_total(horas_trabajo, dinero_horas):
    return "\nhoras de trabajo: " + horas_trabajo + "\nCoste por horas: " + dinero_horas + "\nImporte total: " + str(int(horas_trabajo) * float(dinero_horas))

if __name__ == "__main__":
    horas_trabajo = (input("Escribe las horas: "))
    dinero_horas = (input("Cuanto cuesta por hora: "))
    print(importe_total(horas_trabajo,dinero_horas))
