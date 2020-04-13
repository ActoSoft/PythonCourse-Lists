tupla=('livi',21,1,23,True)
lista=['livi',21,1,23,True]
tupla_2= ('felipe',20,'es bebe')
#una tupla es inmutable
print(tupla + tupla_2)
lista[1] = 25
#tupla[1] = 26
print(tupla)
print(lista)

#if 'livi' in tupla:
    #print('si estoy')
#print(len(tupla))
#for x in tupla :
    #print(x)

print(tupla.count('livi'))
print(tupla.index(True))

print(tupla)
print(lista)

nueva_tupla = tuple(('valor1',1,2,3.0,True))
print(nueva_tupla)