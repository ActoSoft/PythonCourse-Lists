#Hacer una funcion que muestre un nombre
#Vamos a tener una lista de nombres
#Por cada nombre en la lista se va a ejecutar la funcion
#Todo esto tambien en una funcion

#Por cada nombre llamar funcion que muestre el nombre
#La primer funcion va a tener nuesta lista y la logica para llamar la segunda funcion
#La segunda funcion va a imprimir un nombre

def mostrar_nombre(nombre):
    print(nombre)

def nombres():
    lista = [
        "Pamela",
        "Raul",
        "Genoveva"
    ]

    for nombre in lista:
        mostrar_nombre(nombre)

nombres()
