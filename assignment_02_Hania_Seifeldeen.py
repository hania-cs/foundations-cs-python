'''Exercise 1:
Write a function that takes an integer from the user and calculates its factorial, 
(The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n)

n = int(input("Enter a number"))
 answer=1
for i in range(1,n+1):
    answer*=i
print(answer)'''
#---------------------------------------------------------------------------------------------------
'''Write a function that takes an integer as an input from the user and finds all its divisors
and stores them in a list.
Example 1: Input: 10, Output: [1, 2, 5, 10]
Example 2: Input: 16, Output: [1, 2, 4, 8, 16]
Example 3: input: 5, Output: []

n=int(input("Enter a number"))
divisors=[]
for i in range(1,n+1):
    if n%i==0:
        divisors.append(i)
    else:
        continue

print(divisors)'''
#-------------------------------------------------------------------------------------------------------------
'''Write a function called reverseString that takes a string as input from the user and returns
the string reversed. You must use a loop to implement the reversal, and you cannot use any
built-in string or list reversal functions.
Example 1: Input: “Hello World”, Output: “dlroW olleH”
Example 2: Input: “oneword”, Output: “droweno” 


user_input=input("Enter a word: ")
rev= ''
for letter in range(len(user_input)-1, -1, -1):
    rev+=user_input[letter]
print(rev)'''

#--------------------------------------------------------------------------------------------------------------------
'''Write a function that takes a list of integers as input from the user and returns a new list
containing only the even numbers from the original list, in the same order.
Example 1: Input: [1, 2, 3, 4, 5, 6], Output: [2, 4, 6]
Example 2: Input: [5, 3, 18, 4, 2, 7, 10], Output: [18, 4, 2, 10]
Example 3: Input: [5, 3, 11, 5, 1, 7, 27], Output: []

user_input = input("Enter numbers separated by spaces: ")  
user_list = user_input.split()  
user_list = [int(x) for x in user_list]
new_list=[]

print(user_list)
for num in range(len(user_list)):
    if user_list[num]%2==0:
        new_list.append(user_list[num])
    else:
        continue
print(new_list)'''
#------------------------------------------------------------------------------------------------------------
'''Write a function that takes a string as input and checks whether it meets the requirements
for a strong password. A strong password should be at least 8 characters long, contain at
least one uppercase letter, one lowercase letter, one digit, and one special character (a
special character is either #, ?, !, $).'''

password=input("Enter your password")
special_chars=['#', '?', '!', '$']
if(len(password)) >=8:
    for letter in password:
        if letter.isupper()==True and letter.islower()==True and letter.isdigit()==True and special_chars in password:
            print("Strong Password")
    else:
        print("Weak password")
else:
    print("Weak password")