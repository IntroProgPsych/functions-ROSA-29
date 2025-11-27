# https://www.w3schools.com/python/python_arguments.asp
# https://www.w3schools.com/python/python_user_input.asp
# https://www.w3schools.com/python/python_casting.asp
# Write a function square(n) that returns the square of the number n (n multiplyed with n).
# Ask the user for a number, call the function, and print the result.
    
# Sample output:

# Input: 5
# Output: 25

# Write your code here:

number=int(input("Input: "))
def greet(n):
    return n*n
result=greet(number)
print("Output:",greet(number))

