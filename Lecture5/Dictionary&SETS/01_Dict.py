
# Dictionary বানানো:

Students = {
    "name_r" : "Rakib" ,
    "age_r" : 30 ,
    "name" : "Shazid",
    "age" : 32,
    "deft" :"CSC"
}

print(Students)

print(type(Students))


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

# # যেকোনো type এর value

all_mixed = {
     "name" : "Shazidul Islam",
     "age" : 20 ,
     "Cgpa" :3.5,
     "Genarel_Sub" : ("Bangla" , "English" , "History"),
     "Group_Sub" : ["Physics" , "Chemistry" , "Math" , ["nested" , "its to much"]]
}

print(all_mixed)


