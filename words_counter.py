#Counting repetition
#First, you need to receive from the user the element to search. This program needs to return the numbers of times that word appears in the list. If the element appears five times, you must print something like Word: word - Count: 5. If the element are not in the list, put 0 in the counter.

"""words = [
  'machine',
  'matter',
  'subset',
  'trouble',
  'starting',
  'matter',
  'eating',
  'matter',
  'truth',
  'disobedience'
  'matter'
]"""

name = input("Input your name: ")
print("Welcome", name)

words = [
  'machine',
  'matter',
  'subset',
  'trouble',
  'starting',
  'matter',
  'eating',
  'matter',
  'truth',
  'disobedience',
  'matter'
]
search = input("Input the name of the value you want to search: ")

if search in words:
    count = words.count(search)
    print(name, "word - count", count, "times")
else:
    print(name, "word - count: 0 times")


