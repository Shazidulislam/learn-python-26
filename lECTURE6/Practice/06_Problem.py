"""
Write a program to calculate the grade of studen from his marks from the following scheme

90 -100 =>EX
80 -90 => A
70-80 => B
70-60 => C
<50 => F
"""

# Write a program to find out wheter a given post is talking about "Harry" or not


marks = int(input("Enter your result : "))
if(marks >= 91 and marks <=100):print("Your grade :EX")
elif(marks >=81 and marks <= 90  ):print("Your Grade is A")
elif(marks >= 71 and marks <=80):print("Your Grade is B")
elif(marks >= 61 and marks <=70):print("Your Grade is C")
elif(marks >= 51 and marks <= 60):print("Your Grade is D")

else : print("Your grade is F")