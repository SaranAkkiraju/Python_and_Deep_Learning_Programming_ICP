# Program1
# Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultant string and print it.
data = input('Enter the input string:')
count = int(input('Enter number of characters to delete:'))

# Storing into a new string after deleting the count of characters
res = data[0:-count]
print(res[::-1])




# Program2
# Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex
str = input('Enter the string:')
newstring = str.replace("python","Pythons")
print(newstring)



# Program3
# Take two numbers from user and perform arithmetic operations on them.
num1 = input('Enter first number:')
num2 = input('Enter second number:')

a = int(num1)
b = int(num2)

print('Addition:',a + b)
print('Subtraction:',a-b)
print('Multiplicaation:',a * b)
print('Division:',a / b)
print('Modulus:',a % b)
print('Exponent:',a ** b)
print('Floor division:',a // b)

