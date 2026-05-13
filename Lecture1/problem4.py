# import os  # os module import করা হচ্ছে

# path = "C:/ai_ml-file/Python"  # যে folder টা দেখতে চাই তার address

# contents = os.listdir(path)  # folder এর সব files ও folders এর list নিয়ে আসছে

# print(f"Contents of {path}:")  # folder এর নাম print করছে

# for item in contents:  # list এর প্রতিটা item এর জন্য loop চলবে
#     print(item)  # একটা একটা করে সব file/folder এর নাম print করছে


# import os module
import os

# find the path
path = "/Recovery"
# listdir the declar path
context = os.listdir(path)


print(f"Contents os {path}")

for i in context:
    print(i)