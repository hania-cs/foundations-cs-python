# Write a Python program that:
# 1. Continuously prompts the user to enter scores until they input -1 to stop.
# 2. Calculates and prints the average of the entered scores (excluding -1).
# 3. If no valid scores are entered (i.e., if the first input is -1), print a message indicating that
# no scores were entered.
num=0
numbers=[] #initialize a list to store numbers in it
while num!=-1: #stops at -1
    num=int(input("Enter a number")) #takes input
    if num!=-1: #as long as the user doesnt enter -1, the list keeps taking the numbers he's entering

        numbers.append(num)
if len(numbers) ==0: #if user entered -1 from the start
    print("no scores entered")
else:

    sum=0
    for number in numbers:
        sum+=number #add all numbers and store them in one variable

    avg=sum/len(numbers) #divide the sum over the length of the list
    print(f"the score average is {avg}")


