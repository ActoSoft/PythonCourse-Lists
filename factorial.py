n = int(input("Input your number: "))

def factorial(n):
    if(n==0):
        return 1
    else:
        return n * factorial(n-1)

print("The factorial of your number is: ", factorial(n))

