#elaboro: liviere mercado manzano
#Usando la siguiente lista, calcule la suma de los números en la lista e imprímala.
#  Debe imprimir un mensaje legible
numbers = [6, 12, 1, 18, 13, 16, 2, 1, 8, 10]
for elementos in numbers:
    print(f"{elementos:10}")
print("________________________________")    
print(f"{sum(numbers):10}" , " es el resultado de la suma")