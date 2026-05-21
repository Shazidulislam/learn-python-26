
# Set এর গাণিতিক Operations:

a ={1 , 2 , 4 , 3 , 5 , 9}
b = {4 , 5 , 6 ,7 , 8 , 9}

# Union — দুটোর সব মিলিয়ে
print(a | b)  # {1,2,3,4,5,6,7,8 , 9}
print(a.union(b))
print(b.union(a))

# Intersection — দুটোতেই আছে এমন
print(a & b) #{4 , 5 ,9}
print(a.intersection(b))


# Difference — a তে আছে b তে নেই
print(a - b) # {1 , 2 , 3}
print(b.difference(a) , "678") #"b থেকে a এর common গুলো বাদ দাও"


# Symmetric Difference — শুধু একটাতে আছে এমন
print(a ^ b , "a ^ b")
print(b ^ a , "b ^ a")  # 2 ta te je common ase oigula bad de ar jara uncommon tader dew
print(a.symmetric_difference(b))



# Set Check করা:
x = {1 , 2 , 3 }
y = {1 , 2 , 3  , 4 , 5 }

print(x.issubset(y) , " x er sokol element y te ase") #True  x er sokol element y te ase
print(y.issubset(x)) #False  y er sokol element x te nai tai false



print(x.issuperset(y) , "issuperset")  # False —  x , y কে ধারণ করে na
print(y.issuperset(x)) # True — y, x কে ধারণ করে?




# isdisjoint() — কোনো common নেই?

print(x.isdisjoint(y)) #False common ase
print(y.isdisjoint(x)) #False common ase