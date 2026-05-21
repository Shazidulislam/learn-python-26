
# 6.Create an empty dictinory . Allow 4 friends to enter their favorite language as value and use key as their names, Assume that the names are unique.

empty_dic = {}

vic1_Name = input("Enter your name : ") 
vic1 = input("Enter your favorite Language")
vic2_Name = input("Enter your name : ") 
vic2 = input("Enter your favorite Language")
vic3_Name = input("Enter your name : ") 
vic3 = input("Enter your favorite Language")
vic4_Name = input("Enter your name : ") 
vic4 = input("Enter your favorite Language")

empty_dic.update({vic1_Name : vic1 ,vic2_Name : vic2 , vic3_Name : vic3 , vic4_Name : vic4})

print(empty_dic)