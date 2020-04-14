def factorial(result , value):
 if(value>0):
  result=factorial(result,value-1)
  result=result*value
 else:
  result=1
 return result
value=int(input("Ingrese el factor a evaluar  \n"))
result=1
result=factorial(result,value)
print ("el factorial es :" , result)
    