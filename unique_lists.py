#Unique lists
#Using the following list, remove the duplicates values, and print the list without any duplicated.

"""words = [
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
]"""

name = input("Input your name: ")
print("Welcome", name)

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
print(words)


alone = []
#words_copy = list(words)

"""for i in words:
    if i not in alone:
        alone.append(i)
    else:
        words.remove(i)

print(words)
print(alone)"""

for i in range(len(words)-1, -1, -1):
    if words[i] not in alone:
        alone.append(words[i])
    else:
        words.remove(words[i])

print(words)
