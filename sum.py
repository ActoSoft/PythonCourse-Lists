#Calculating a sum
#Using the folowing list, calculate the sum of the numbers into the list and  it. You should print a readable message like The sum of the numbers is: n
# numbers = [6, 12, 1, 18, 13, 16, 2, 1, 8, 10]

name = input("Input your name: ")
print("Welcome", name)

numbers = [6, 12, 1, 18, 13, 16, 2, 1, 8, 10]

average = sum(numbers)
#print(name, "the sum of yours numbers is: ", average) "firt method"

print(name, f"the sum of yours numbers is: {average:.2f}") #it´s the same only with floating point

#The end



