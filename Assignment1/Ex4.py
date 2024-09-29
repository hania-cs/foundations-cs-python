# A four-digit number ABCD is said to be lucky if A + B = C + D
# 1. write a program that reads a number(int) from the user
# 2. checks if it was lucky or not
# 3. it should print "F" if it was lucky, otherwise print "U"

num=int(input("enter a number: "))

D=num%10 #get the last number
C=(num/10)%10 #get the third number
B=(num/100)%10 #get the second
A=(num/1000)#get the third
if A+B==C+D:
    print("f")
else:
    print("U")