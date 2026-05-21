
# Write a program to find out whether a student has passed of failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subject and take marks as an input from the user

physics = int(input("Enter your physics Number : "))
chemistry = int(input("Enter your chemistry Number : "))
bilogy = int(input("Enter your bilogy Number : "))

percentage  = (physics + chemistry + bilogy)/300 *100 

print(percentage  ,"%") 

if percentage >= 40 and physics >=33 and chemistry >= 33 and bilogy>=33 : 
    print(f"Student has Passed , found {percentage}")
else : print("Student has Failed")    