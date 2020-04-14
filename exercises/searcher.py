#elaboro: liviere mercado manzano
# recibir del usuario el elemento para buscar. Con ese elemento, busque en la siguiente lista si el elemento existe. 
# Si existe, imprima la posición del elemento en la lista
#  si no existe, imprima un mensaje como Element not found
words = [
  'machine',
  'subset',
  'trouble',
  'starting',
  'matter',
  'eating',
  'truth',
  'disobedience'
]

words_index = words.index(input('INGRESA PALABRA A BUSCAR:  '))
print("SE ENCUENTRA EN EL INDICE: " , words_index)

