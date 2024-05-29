import random

numeros = list(range(1, 101))

print("Adivina el numero secreto del 1 al 100")

numero_aleatorio = random.choice(numeros)

while True:
    usuario_adivinanza = int(input("¿Qué número crees que es?: "))

    if usuario_adivinanza > numero_aleatorio:
        print("El número es más pequeño")

    elif usuario_adivinanza < numero_aleatorio:
        print("El número es más grande")
        
    else:
        print("¡Lo adivinaste! El número aleatorio era: ",numero_aleatorio)
        break

