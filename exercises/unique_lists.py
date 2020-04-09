#Usando la siguiente lista
# elimine los valores duplicados e imprima la lista sin ningún duplicado.
words = [
  'crab',
  'poison',
  'contagious',
  'simple',
  'bring',
  'sharp',
  'playground',
  'poison',
  'communion',
  'simple',
  'bring'
]

palabra_count = words.count(input('Cual es la palabra a verificar? : '))
print("se repite : " , palabra_count , "veces")
elemento =  words . pop (palabra_count)
words.pop(palabra_count)
print(words)

#solo pude quitar unode la lista :')