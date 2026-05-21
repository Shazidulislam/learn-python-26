

# Set এ Add ও Remove:
fruits = {"Apple" , "Banana"}
print(fruits)
# add 
fruits.add("Mango")
print(fruits)
# অনেকগুলো add
fruits.update(["Grape" , "Kiwi" , "Pynapal"])
print(fruits)



# # remove — না থাকলে error
# fruits.remove("Kiwis")
# print(fruits)


# discard — না থাকলেও error নেই
fruits.discard("xuyrv")
print(fruits)
fruits.discard("Kiwi")
print(fruits)

removed = fruits.pop()  # random একটা বের করে
print(removed)  # যেকোনো একটা
print(fruits)   # বাকিগুলো

removed = fruits.pop()  # random একটা বের করে
print(removed)  # যেকোনো একটা
print(fruits)   # বাকিগুলো
# ⚠️ Set unordered তাই কোনটা বের হবে বলা যায় না!

# . copy() — set এর copy বানায়
fruits_copy = fruits.copy()
print(fruits_copy)  # {'apple', 'banana', 'mango'}


# সব remove
fruits.clear()
print(fruits)