
# Write a program to accept make of 6 studens and then in a sorted manner

stduents = []

stduent1 = int(input("Enter 1st student result : "))
stduent2 = int(input("Enter 2st student result : "))
stduent3 = int(input("Enter 3st student result : "))
stduent4 = int(input("Enter 4st student result : "))
stduent5 = int(input("Enter 5st student result : "))
stduent6 = int(input("Enter 6st student result : "))

stduents.extend([ stduent1 ,stduent2 , stduent3 , stduent4 , stduent5 , stduent6 ])

print(stduents)
stduents.sort()
print(stduents)

