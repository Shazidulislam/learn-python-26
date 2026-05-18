
nested = [1, 2, [3, 4, 5]]
#                ^^^^^^^^— ভেতরের list

# ক্লাসের রোল ও নাম
students = [
    ["Rakib", 20, "CSE"],
    ["Shazid", 21, "EEE"],
    ["Karim", 22, "ME"]
]


# Nested List Access করা:

print(students[0])
print(students[0][0])
print(students[1][1])
print(students[2][1])

# Nested List এ Add ও Remove:

students.append("Ad something")
print(students)

students.append(["Karim", 22])
print(students)

# প্রথম student এর বয়স পরিবর্তন
students[0][1] = 25
print(students[0])  # ['Rakib', 25]


# একটা student remove
students.remove(["Shazid", 21])
print(students)
# [['Rakib', 25], ['Karim', 22]]

