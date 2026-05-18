
# Dictionary Access:

students = {
    "name" : "Shazidul",
    "age" : 20 ,
    "dept" : "CSE"
}
# key দিয়ে access
print(students["name"])
print(students["dept"])

# get() দিয়ে access — না থাকলে error দেয় না
print(students.get("name")) 
print(students.get("age"))
print(students.get("noting")) # নেই — default value


# Dictionary Add ও Update:

marks = {
    "Physics" : 89,
    "Chemistry" : 84 , 
    "Biolozy" : 70,
    
}
# নতুন key-value add
marks["group"] = "Science"
print( marks)

# value update
marks["Physics"] = 93
print(marks["Physics"])

# update() দিয়ে একসাথে অনেকগুলো  & নতুন add kora jai
marks.update({"Chemistry" : 80 , "age" : 21 , "Love" : "Allah"})
print(marks)


