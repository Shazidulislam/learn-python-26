# Write a program which findes out whether a given name is present in a list or not

name_list = ["Shazid" , "Rahim" , "Karim" , "Sakib"]

name = input("Enter a name : ")

if name in name_list : print(f"{name} is present in the list")

else: print(f"{name} is not present in this list")