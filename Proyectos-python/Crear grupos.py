import random

# Ingrese en esta lista todos los nombres
nombres = ['nombre1', 'nombre2', 'nombre3', 'nombre4', 'nombre5', 'nombre6']

while True:
    respuesta = input(
        "Presiona enter para hacer un grupo aleatorio o 's' para salir: ")

    if respuesta == 's':
        print("Hasta la próxima")
        break

    elif respuesta == '':

        x = int(input("¿De cuántas personas quiere hacer los grupos?: "))

        lista = min(len(nombres), x)
        grupo = random.sample(nombres, lista)
        nombres = [nombre for nombre in nombres if nombre not in grupo]

        print(grupo)
