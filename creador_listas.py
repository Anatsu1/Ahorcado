import os

print("//////////////////////////////////////////////////////////////////")
Decision = input("Desea iniciar el creador de listas? ")
decisiones = ["si", "Si", "sI", "SI"]
os.system ("cls")
if Decision in decisiones:
    lista_def = []

while True:
    print("//////////////////////////////////////////////////////////////////")
    palabras = input("ingrese las palabras: ")
    print("//////////////////////////////////////////////////////////////////")
    lista = palabras.split()
    for palabra in lista:
        os.system ("cls")
        lista_def.append(palabra)
        print(lista_def)

#Este lo cree meramente para crear las listas de palabras para el ahorcado, recomiendo que esten todas en horizontal.