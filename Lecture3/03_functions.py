
name = "Shazidul"
# Case Related Functions
'''
print(len(name))


print(name.capitalize())

print(name.upper())

print(name.lower())

print(name.swapcase())
'''
# 2. Search Related Functions
# nums = "Shamin Ahasun Shazid"
'''
print(nums.find("haz"))  # 15 — কোন index এ আছে
print(nums.index("haz")) # 15 — find এর মতো কিন্তু না পেলে error

print(nums.count("h"))  # 3 — কতবার আছে

print(name.endswith("dul"))
print(name.endswith("DUL"))
print(name.startswith("sha"))
print(name.startswith("Sha"))
'''

# 3. Remove Space Functions
# nums = "  Shamin Ahasun Shazid  "

# print(nums.strip()) # "Shamin Ahasun Shazid" — দুইপাশের space বাদ
# print(nums.lstrip()) #"Shamin Ahasun Shazid   " — বামের space বাদ
# print(nums.rstrip())# "   Shamin Ahasun Shazid" — ডানের space বাদ



# 4. Replace & Split Functions

num = "Shamin Ahasun Shazid"

# print(num.replace("Shazid" , " "))
# print(num.split(" "))
# print(num.split("h"))

# 5. Check Related Functions

str = "string is here"
number = "123"
str_num = "shazidul910"

print(str.isalpha()) # False — শুধু অক্ষর?
print("Hellopython".isalpha()) # True  — শুধু অক্ষর?

print(number.isdigit())   # True  — শুধু সংখ্যা?
print(str_num.isalnum())  # True  — অক্ষর বা সংখ্যা?
print(number.isalnum())  # True  — অক্ষর বা সংখ্যা?

print("   ".isspace())      # True  — শুধু space?
print("HELLO".isupper())    # True  — সব বড় হাতে?
print("hello".islower())    # True  — সব ছোট হাতে?
print("Hello World".istitle()) # True — Title case?

# 6. Join & Format Functions
