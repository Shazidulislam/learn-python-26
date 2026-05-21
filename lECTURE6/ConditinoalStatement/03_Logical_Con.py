
#  Logical Operator দিয়ে Multiple Condition

age = int(input("Enter your age : "))
marks = int(input("Enter your total Marks : "))
citizen = True

# and , দুটো শর্তই True হতে হবে

if (age >= 18 and citizen==True):{
    print("Now you are adult"),
    print("You can vote!")
}

if(age >=18 and marks >=90):{
    print("You should apply for scholarship!"),
    print("Shcolarship pabe!")
}

# or যেকোনো একটা True হলেই হবে
if(age >=18 or marks>=70):
    print("Now you can go college!"),
    print("now you passed!")
    
    
    # # not — উল্টো করে
if not age <18 :
    print("Adult")

#   in দিয়ে Condition

fruits = ["apple" , "banana" , "mango"]

if "apple" in fruits:
    print("We have an apple order") 
    
else:print("we don't have any order!")  

if 'grap' not in fruits :
    print("Graps not found")
else:print("We found grap")    