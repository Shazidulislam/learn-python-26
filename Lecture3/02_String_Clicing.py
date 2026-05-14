a = "0123456789"

print(a[::2])      # Start to end, take every 2nd character
# Output: 02468

print(a[1:7:3])    # Start from index 1 to 6, take every 3rd character
# Output: 14


b = "abcdefghijklmnopqrstuvwxyz"

print(b[0::4])     # Start from index 0, take every 4th character
# Output: aeimquy

print(b[:25:6])    # From start to index 24, take every 6th character
# Output: agmsy


print(len(a))      # Length of string a
# Output: 10

print(len(b))      # Length of string b
# Output: 26
