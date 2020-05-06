
#Hacer una calculadora con puras funciones

#Aqui se definen las funciones
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def division_exacta(num1, num2):
    return num1 // num2

def elevar_cuadrado(num1):
    return num1 **2

#primero se va a recibir el nombre de lo que se esta imprimiendo "name" y despues el valor que se esta recibiendo para imprimir
def print_values(name, value):
    print(f"El resultado de la {name} es {value}")

#Esta funcion se llama para inicializar el programa
def main():
    num1 = float(input("Dame el numero 1: "))
    num2 = float(input("Dame el numero 2: "))

    sumaa = suma(num1, num2)
    restaa = resta(num1, num2)
    multi = multiplicacion(num1, num2)
    divi = division(num1, num2)
    div_exacta = division_exacta(num1, num2)
    cuadrado1 = elevar_cuadrado(num1)
    cuadrado2 = elevar_cuadrado(num2)

    print_values("suma", sumaa)
    print_values("resta", restaa)
    print_values("multiplicacion", multi)
    print_values("division", divi)
    print_values("division_exacta", div_exacta)
    print_values("elevar_cuadrado", cuadrado1)
    print_values("elevar_cuadrado", cuadrado2)

main()