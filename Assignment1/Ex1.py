# Write a Python program that asks the user to input 3 numbers,
# and then the program will find and print the maximum value among the entered numbers.


#user enters three numbers

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter the third number"))

if num1>num2 and num1>num3:
    print(f"{num1} is the largest number") #if num1 is larger than both numbers, num1 gets printed out

elif num2>num1 and num2>num3:
    print(f"{num2} is the largest number") #if num2 is larger than both numbers, num2 gets printed out

else:
    print(f"{num3} is the largest number") #if num3 is larger than both numbers, num3 gets printed out