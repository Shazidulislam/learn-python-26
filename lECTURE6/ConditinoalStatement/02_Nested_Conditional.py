
# . Nested if (if এর ভেতরে if)
# age = int(input("Enter you real age : "))
age =20
citizen = True

if age >=18 :
    if citizen== True :
        print("Now You can vote")
    else:print("Not thus form this nation!")
else : print("You are under age!")        
        
        
        
#  Short Hand if (One Line)
if age >=18 :print("Adult")


# Ternary Operator
your_age = int(input("Your age : "))
result = "Adult , Now you can vote!" if your_age>=18 else "Minor"

print(result)

name = input("Enter your name : ")
my_name = f"I am {name}ul" if name.lower() == "shazid" else f"I am {name}"

print(my_name)
    



