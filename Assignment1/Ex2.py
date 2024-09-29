# Write a Python program that:
# 1. Takes a positive integer n from the user.
# 2. Multiplies all the odd numbers between 1 and n (inclusive).
# If the product exceeds 100, print "Multiplication exceeded" and stop the multiplication process.
# If there are no odd numbers, the program should simply return 1.
# If the multiplication process completes without exceeding 100, print the final product.

result=1 #initialize var 
odd=False #boolean var to check if a number is odd or even set to False

num=int(input("Enter a positive number")) #take input from user
for i in range(1,num+1): #loop through the numbers from 1 to num
    if i%2==0: #skip even numbers
        continue
    odd=True #set odd to True
    result*=i #nultiply numbers between 1 and num
    if(result>100):
        print("multiplication exceeded")
        break #breaks the loop
if not odd: #if no odd numbers print 1
    print(1)
elif (result<=100):
    print(result) #print final result if < 100