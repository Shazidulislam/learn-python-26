
# Check that a type cannot be changed in python

my_tuple = (1 , 2  ,3 , "Unmuteable" , "Not change type" , True)

print(my_tuple)
print(type(my_tuple))

my_list = list(my_tuple)
my_list[3] = "Muteable"
print(my_list)


# খালি dictionary
empty = {}

print(empty)

# dict() দিয়ে
person = dict(name="Shazidul" , age = 20)

print(person)
print(type(person))

mixed = dict(name = "Shazidul" , 
             age = 20,
             cgpa = 3.99,
             subjects = ["Math" , "Physics"]
             )

print(mixed)