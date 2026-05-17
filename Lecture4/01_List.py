
friends = ["Apple" , "Orange" , 5 , 40.56 , False ,"Aakash" , "Lubna" ]

print(friends[2])

friends[2] = 400 #List are mutable 

print(friends[2])
print(friends)

# nested list

nested = ["Shazid" , 490 , [3 , True , 40.90 , "Shamim"] , "Brother"]

print(nested[2])

# List Access
fruits = ["apple" , "banna" , "mango" , "orange"]
print(fruits[-1])

print(fruits[::2])






#List e Add kora 

my_friends = ["Mango" , "Beef" , "Mutton" , "Kacchi" ]

my_friends.append("Mahir") ## শেষে add করে
print(my_friends)

my_friends.insert(0 , "Pynapal")
print(my_friends)

# my_friends.extend(["Hello" , "Python" , "Nothing"])
# print(my_friends)

my_friends = ["Shanto" , "Mim"] + my_friends

print(my_friends)













# List থেকে Remove করা:
my_friends.remove("Beef")# নাম দিয়ে remove
print(my_friends)
my_friends.pop() # শেষেরটা remove
print(my_friends)
my_friends.pop(3) # index দিয়ে remove
print(my_friends)

my_friends.clear() # সব remove
print(my_friends)











# List এর অন্যান্য Functions:
numbers = [3, 1, 4, 2, 1, 5, 9, 2]
print(len(numbers)) #কতটা item
print(numbers.count(2))  # 2  কতবার আছে
print(numbers.index(4))  #  4 কোন index এ
numbers.sort() 
print(numbers)



numbers.reverse()
print(numbers)


