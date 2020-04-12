#Find the maximum
#Receive two numbers (from keyboard) and print the largest one. If both numbers are the same print a message related to both are the same.

name = input("Input your name: ")
print("Welcome", name)

num_Uno = float(input(name + " input your first number: "))
num_Dos = float(input(name +  "input your second number: "))

if num_Uno > num_Dos:
    print(name , "the largest number is the first with: ", num_Uno)
elif num_Dos > num_Uno:
    print(name , "the largest number is the second with: ", num_Dos)
else:
    num_Uno = num_Dos
    print(name , "both numbers are the same")


"""if num_Uno < num_Dos:
    print(name , "the largest number is the second with: ", num_Dos)
elif num_Dos < num_Uno:
    print(name , "the largest number is the first with: ", num_Uno)
else:
    num_Uno = num_Dos
    print(name , "both numbers are the same")"""

