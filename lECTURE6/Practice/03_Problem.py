
# 3. A spam comment is defined as a text containing following keywords :
# "Make a lot of money" , "Buy now" , "Subscribe this" , "Click this" , Write a program to detect the program

# spam comment detector

comment = input("Enter your comment : ")

if(comment in "Make a lot of money" 
   or "Buy now" in comment or
   "Subscribe this" in comment or
   "Click this" in comment
   ):print(f"{comment} \n it's a spam comment.")

else : print("It't not a spam comment.")