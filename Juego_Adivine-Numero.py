# DESCRIPCIÓN JUEGO:
#Va a crear un programa que va a escoger un número aleatoriamente, entre 0 y 99, 
# y a continuación, le va a pedir al usuario que adivine este número.

#Tras cada intento, le responderá indicándole si se ha quedado corto o se ha pasado,
#  hasta que encuentre el número.
# Entonces, mostrará el número de intentos que han hecho falta para encontrar este número 
# y el programa se terminará.

import random

numero = random.randint(0,100)
print("Vamos a jugar a un juego, voy a pensar un numero entre el 0 y el 99 y lo tienes que adivinar")

i = 0 #contador de intentos

while True: ##BUCLE INFINITO del que solo saldremos cuando acertemos el numero
    #pedimos al usario que nos diga un número
    intento = input("Dime un número entre 0 y 99: ")
    i = i+1 #incrementamos el contador de intentos
    
    try: #intentamos convertir el input a entero
        intento = int(intento)
    except: #si no se puede convertir, avisamos al usuario y repetimos el bucle
        print("No has introducido un número")
        continue

    #puede ser que sea menor que el número deseado
    if intento < numero:
        print("Te has quedado corto, prueba otra vez")
        pass
    
    #o mayor
    elif intento > numero:
        print("Te has pasado, prueba otra vez")
        pass

    else: #CONDICIÓN PARA SALIR DEL BUCLE INFINITO
        if intento == numero: #si el usuario acierta el número
            break

#Una vez hemos salido del bucle, es porque hemos acertado el número
print("Has acertado, el número es el", numero, "y has necesitado", i, "intentos para adivinarlo")
