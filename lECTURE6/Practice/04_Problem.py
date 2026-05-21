
# Write A program to find whether a given username contains less then 10 characters or not

userName = input("Enter your name : ")

length = len(userName)

if length < 10 : print(f" {userName} length {length}\n less then 10")
else:print(f"{userName} , the length is out of 10 ,\n length is {length}")