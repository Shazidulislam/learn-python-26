# Write a program to input eight numbers from the user and dislplay all the unique numbers(once)

unique_numbers = set()

num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2st number : "))
num3 = int(input("Enter the 3st number : "))
num4 = int(input("Enter the 4st number : "))
num5 = int(input("Enter the 5st number : "))
num6 = int(input("Enter the 6st number : "))
num7 = int(input("Enter the 7st number : "))
num8 = int(input("Enter the 8st number : "))

unique_numbers.update([num1 , num2 , num3 , num4 , num5 , num6 , num7 , num8])

print(unique_numbers)