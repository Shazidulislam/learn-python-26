
# Dictionary Remove:
student = {"name" : "Shamim Ahausn Shazid",
            "age" : 20 ,
            "dept" : "CSE" ,
            "position" : "Buisness"
           }

print(student)

# নির্দিষ্ট key remove
del student["position"]
print(student)

# pop() দিয়ে remove — value ও return করে
print(student.pop("dept"))  # CSE

print(student)


# সব remove
student.clear()

print(student)




# Dictionary Methods:

print(student.keys())    # dict_keys(['name', 'age', 'dept'])
print(student.values())  # dict_values(['Rakib', 20, 'CSE'])
print(student.items())   # dict_items([('name','Rakib'),...])
print(len(student))  
