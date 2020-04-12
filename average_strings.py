#Mid Level: list of strings
#Find the average length of the following list of strings
"""words = [
    'seat',
    'correspond',
    'linen',
    'motif',
    'hole',
    'smell',
    'smart',
    'chaos',
    'fuel',
    'palace'
]"""

from statistics import mean

name = input("Input your name: ")
print("Welcome", name)

words = [
    'seat',
    'correspond',
    'linen',
    'motif',
    'hole',
    'smell',
    'smart',
    'chaos',
    'fuel',
    'palace'
]

total = 0

"""for i in words:
    total += len(i)
average = float(total) / float(len(words))
print(name, f"the average length of the following list of strings is: {average:.2f}")""" #First method

print(mean([len(i) for i in words])) #Shorter method





