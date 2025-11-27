# https://www.w3schools.com/python/python_casting.asp / https://www.w3schools.com/python/python_scope.asp
# Write a function add(a, b) that returns the sum of the two numbers.
# Ask the user for two numbers (as input), convert them to integers, call the function, and print the result.
    
# Write your code here:
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
def add(a,b):
    return a+b
print("The sum is:",add(a,b))
