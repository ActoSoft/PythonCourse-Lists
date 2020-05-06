#Finding Longest Word
#Using the following list, you need to find the longest word into the list and print it. If there are 2 or more with the same length, you must print only the first ocurrence.
"""words = [
  'mystery',
  'brother',
  'aviator',
  'crocodile',
  'pearl',
  'orchard',
  'crackpot'
]"""

name = input("Input your name: ")
print("Welcome", name)

words = [
  'mystery',
  'brother',
  'aviator',
  'crocodile',
  'pearl',
  'orchard',
  'crackpot'
]

def longest_word(words):
  len_word = []

  for w in words:
    len_word.append((len(w), w))
  
  #print(len_word)

  len_word.sort()

  #print(len_word)

  return len_word[-1][1]

print(name, "the longest word is:", longest_word(words))





