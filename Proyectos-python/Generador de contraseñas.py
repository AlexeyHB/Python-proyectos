import random
import string

while True:

    letras_y_numeros = string.ascii_letters + string.digits

    x = input(
        "Presiona enter para generar una contraseña aleatoria o 's' para salir: ")

    if x == '':
        tamaño_contraseña = int(
            input("Cuantos caracteres quieres que sea de largo la contraseña?: "))

        contraseña = ''.join(random.choices(
            letras_y_numeros, k=tamaño_contraseña))

        print(contraseña)

    elif x == 's':
        print("Hasta la proxima")
        break
