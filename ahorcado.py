#Declaracion de librerias y variables
import os
import time
import random  
puntaje = 0
puntaje_maximo = 0
jugar_de_nuevo  = True
jugar_negativo = ("No","no","nO","NO","n","N")
jugar_positivo = ("Si","si","sI","SI","s","S")
lista_palabras = ['animal', 'perro', 'gato', 'vaca', 'cerdo']

img_ahorcado = (
r'''
    +---+
    |   |
        |
        |
        |
        |
===========''', 
r'''
   +---+
   |   |
   O   |
       |
       |
       |
==========''', 
r'''
   +---+
   |   |
   O   |
   |   |
       |
       |
==========''', 
r'''

   +---+
   |   |
   O   |
  /|   |
       |
       |
==========''', 
r'''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
==========''', 
r'''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
==========''', 

r'''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========='''
)

def eleccion_img (f):
    print(img_ahorcado[f])

os.system ("cls")

#Bienvenida al jugador

print("///////////////////////////////////////////////////")
nombre = input("Hola! Por  favor ingrese su nombre: ")
print("Hola, " + nombre + " es hora de jugar al ahorcado")
time.sleep(1)
print("Comienza a adivinar!")
print(" ")
eleccion_img(6)
time.sleep(2)
os.system ("cls")

#Inicio del programa
while jugar_de_nuevo == True:

    #Declaracion de variables dentro del bucle por posible rejuego
    letras_probadas = []
    juego_no_terminado = True
    letras  = " "
    vidas = 6
    fallos = 0

    #Obtencion de palabra random
    cantidad_palabras = len(lista_palabras)
    palabra_random = random.randint(0, cantidad_palabras - 1) 
    palabra = lista_palabras[palabra_random] 
    lista_palabras.remove(palabra)
    

    #Bucle de reconocimiento e impresion de la palabra clave
    while vidas > 0:
        fallas = 0
        eleccion_img(fallos)
        for letra in palabra:

            if letra in letras:
                print(letra,end = " ")

            else:
                print("_",end = " ")
                fallas = fallas + 1 

        #Sentencia de reconocimiento de victoria del jugador        
        if fallas == 0:
            os.system ("cls")
            eleccion_img(fallos)
            print("Felicidades, ganaste!")
            puntaje = puntaje + 100

            #Correcion del puntaje maximo
            if puntaje >  puntaje_maximo:
                puntaje_maximo = puntaje  
            break
        
        print(" ")
        print(" ")

        #Recoleccion de letras insertadas  
        while True:
            print ("Letras probadas: ", end = " ")
            print(letras_probadas)
            tu_letra = input("introduce una letra:")
            letras += tu_letra
            tu_letra = tu_letra.lower()
            if len(tu_letra) != 1:
                print("Por favor, introduce una letra.")
            elif tu_letra in letras_probadas:
                print('Ya has probado esa letra. Elige otra.')
            elif tu_letra not in "abcdefghijklmnñopqrstuvwxyz":
                print('Por favor ingresa una LETRA.')
            else:
                letras_probadas.append(tu_letra)
                break
            
        time.sleep(0.5)
        os.system ("cls")

        #Sentencia de reconocimiento de letras dentro de la palabra clave
        if tu_letra not in palabra:
            vidas = vidas - 1
            v = str(vidas)
            fallos = fallos + 1
            eleccion_img(fallos)
            print("Te equivocaste.")
            print("Vidas restantes:",end= " ")
            print( v )
            print(" ")
            time.sleep(1.5)
            os.system ("cls")

        #Sentencia  de perdida total de vidas
        if vidas ==  0:
            os.system ("cls")
            eleccion_img(fallos)
            print("Te quedaste sin vidas!")
            print("La palabra era: ", "---" ,end= " ")
            print(palabra ,end= " " )
            print("---")
            puntaje = 0

    #Pantalla final y posible rejuego
    print("Gracias por participar!")
    print("Tu puntaje es de: ", puntaje)
    print("Tu puntaje maximo es de: ", puntaje_maximo)
    print(" ")

    #Bucle de procesamiento de decision
    while juego_no_terminado == True:
        print("¿Quieres jugar nuevamente?")
        jugar_nuevamente = input ("Si o No:")
        if  jugar_nuevamente in jugar_negativo:
            juego_no_terminado = False
            jugar_de_nuevo = False
            time.sleep(1)
            os.system ("cls")
        elif jugar_nuevamente in jugar_positivo:
            juego_no_terminado = False
            time.sleep(2)
            os.system ("cls")
        else:
            print("Ingrese una respuesta valida")