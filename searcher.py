#Finding an element in an list
#Lets create a simple searcher.
#First, you need to receive from the user the element to search. With that element, search into the following list if the element exist. If it exist, print the position of the element into the list, if not exist print a message like Element not found or something like that.

"""words = [
  'machine',
  'subset',
  'trouble',
  'starting',
  'matter',
  'eating',
  'truth',
  'disobedience'
]"""

name = input("Input your name: ")
print("Welcome", name)

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

search = input("Input the name of the value you want to search: ")

if search in words:
    index = words.index(search)
    print(name, "the element exist in the position: ", index)
else:
    print(name, "the element does not exist")


