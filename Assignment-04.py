'''
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

try:
    file1 = open('sample.txt','r')
    reading_file = file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("The  file 'sample.txt' was not found.")

'''
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

'''
file = open('output.txt','w')
writing = input('Enter text to write to file: ')
file.write(writing)
print('Data successfully written to output.txt')
file.close()
file = open('output.txt','a')
appending = input('Enter additional text to append: ')
file.write(appending)
print('Data successfully appended to output.txt')
file.close()
file = open('output.txt','r')
print('final content of output.txt :',file.read())
file.close()