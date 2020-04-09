#Reciba dos números (desde el teclado) e imprima el más grande. Si ambos números son iguales
#  imprima un mensaje relacionado con ambos son iguales.
valor1=int(input("Ingrese primer valor: "))
valor2=int(input("Ingrese segundo valor: "))
if valor1 > valor2:
    print(valor1 ,'es mayor')
elif valor1 < valor2:
    print(valor2 ,'es mayor')
elif valor1 == valor2:
    print('son iguales')         