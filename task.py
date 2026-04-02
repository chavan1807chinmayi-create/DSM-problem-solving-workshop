# phy = 30, 4, 55, 78, 88
# chem = 40, 50, 60, 70, 80
# maths = 50, 60, 70, 80, 90
# gender = input("Enter your gender: ")
# total = sum(phy) + sum(chem) + sum(maths)
# percentage = total / 15
# print("Total marks: ", total)
# print("Percentage: ", percentage)
# if percentage >= 60 and gender.lower() == "male":
#     print("You are eligible for placement.")    
# else:    
#     print("You are eligible for data entry job.")
    
marks_phy = int(input("Enter marks in physics: "))
marks_chem = int(input("Enter marks in chemistry: "))
marks_maths = int(input("Enter marks in maths: "))
gender = input("Enter your gender: ")
total = marks_phy + marks_chem + marks_maths
percentage = total / 3
print("Total marks: ", total)
print("Percentage: ", percentage)
if percentage >= 60:
    print("You are eligible for placement.")
else:
    print("You are eligible for data entry job.")

