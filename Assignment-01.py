'''
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
'''

a= input('Enter your first number : ')
b= input('Enter your second number : ')

a = int(a)
b = int(b)


c= a+b
print('Addition: ',c)

d= a-b
print('Subtraction: ',d)

e= a*b
print('Multiplication: ',e)

f= a/b
print('Division: ',f)



'''
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''

a= input('Enter your first name : ')
b= input('Enter your last name : ')


print('Hello, ',a,' ',b,"! Welcome to the Python program")
