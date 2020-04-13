def factorial(a,b):
 if(b>0):
  a=factorial(a,b-1)
  a=a*b
 else:
  a=1
 return a
b=int(input("Ingrese el factor a evaluar  \n"))
a=1
a=factorial(a,b)
print ("el factorial es :" , a)
    