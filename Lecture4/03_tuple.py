
# Tuple বানানো:
my_tuple = ()

single  = (2,)

print(my_tuple , single)

mixed = (1 , "Rakib" , 3.12 , True , "UnMuteable")

print(mixed)

nested = (1 ,2 , 3, (4 , 5 , 6) , 6 , 7)

print(nested)


# Tuple Access:
colors = ("red" , "drak" , "green" , "blue" , "yello" , "pupel" , "white")

print(colors[0])
print(colors[-1])
print(colors[0:2])
print(colors[0::2])


numbers = (3, 1 , 4 ,6 ,9 ,7 ,14 , 12.5)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

list = [1 , 3 ,34 , 2 , 9 , 4 ,8 , 23 , 12  ]

list.sort()

list.reverse()

print(list)






# # Tuple এর Functions:

# numbers = (1 ,4 , 3 , 5 , 6 ,9 , 7 ,1)

# print(len(numbers)) # 5 — কতটা item
# print(numbers.count(1))  # 2 — 1 কতবার আছে
# print(numbers.index(4))    # 1 — 4 কোন index এ

# # Tuple পরিবর্তন করা যায় না:
