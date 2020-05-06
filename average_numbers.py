#Calculate the Average
#You already know how to calculate the average of a group of numbers.

#Jr Level: list of numbers
#Find the average of the numbers into the following list
#numbers = [2, 6, 9, 10, 7, 4, 1, 9]

name = input("Input your name: ")
print("Welcome", name)

numbers = [2, 6, 9, 10, 7, 4, 1, 9]

average = sum(numbers) / len(numbers)

#print(name, f"the average of yours numbers is: {average:.2f} ") first method

print(name, "the average of yours numbers is: " , average) #this is the same as the previous line only with decimal point