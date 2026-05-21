# Write a program to find the gretest of four numbers enterd by user.


num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
num4 = int(input("Enter number 4 : "))

if (num1>=num2) and (num1>=num3) and (num1 >= num4 ) :
    gretest = num1
elif (num2>=num1) and (num2>=num3) and (num2 >= num4 )  : 
    gretest = num2
elif (num3>=num1) and (num3>=num2) and (num3 >= num4 )  : 
    gretest = num3
else: gretest = num4

print(f"The gretest number : {gretest}")