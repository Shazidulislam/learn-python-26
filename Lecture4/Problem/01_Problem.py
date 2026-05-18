# write a program to store seven fruits in a list entered by user.


# make a empty list 

fruits = []
print(fruits)

fruits1 = input("Store your 1st fruit :  ")
fruits2 = input("Store your 2nd fruit :  ")
fruits3 = input("Store your 3rd fruit :  ")
fruits4 = input("Store your 4th fruit :  ")
fruits5 = input("Store your 5th fruit :  ")
fruits6 = input("Store your 6th fruit :  ")
fruits7 = input("Store your 7th fruit :  ")

fruits.extend( [fruits1 , fruits2 , fruits3 , fruits4 , fruits5 , fruits6  , fruits7] )

print(fruits)



