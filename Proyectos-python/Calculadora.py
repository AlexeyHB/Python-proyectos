while True:

    operacion = input(
        "¿Qué operación desea realizar? Suma/Resta/Multiplicacion/Division/Porcentaje o 's' para salir:  ")

    lista = ["Suma", "Resta", "Multiplicacion", "Division", "Porcentaje", "s"]

    while operacion not in lista:
        operacion = input(
            "Error, eliga una opción válida (Suma/Resta/Multiplicacion/Division/Porcentaje) o 's' para salir: ")

    if operacion == "s":
        break

    n1 = int(input("Ingrese el primer número o porcentaje: "))
    n2 = int(input("Ingrese el segundo número: "))

    Suma = n1 + n2
    Resta = n1 - n2
    Multiplicacion = n1 * n2
    Division = n1 / n2
    Porcentaje = n1 % n2

    if operacion == "Suma":
        print(Suma)

    elif operacion == "Resta":
        print(Resta)

    elif operacion == "Multiplicacion":
        print(Multiplicacion)

    elif operacion == "Division":
        print(Division)

    elif operacion == "Porcentaje":
        print(Porcentaje)
