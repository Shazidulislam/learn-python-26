# write a program to detect double space in a string

text = "Here is a double  space  s"
print(text.count("  "))
print(text.find("  "))
print(text.replace("  " , " "))


# Replace the double space from problem 3 with single space

text1 = "Onek time     ek ba  ekdik  space   thakte pare"
print(text1.find("  "))
print(" ".join(text1.split()))
print(text1.count("    "))


