
# # Example:
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")


# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade: A")   
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# a = 11
# b = 10
# c = 4
# if a > b:
#     if a > c:
#         print("a is the greatest")
#     else:
#         print("c is the greatest")
# elif b > a:
#     if b > c:
#         print("b is the greatest")
#     else:
#         print("c is the greatest")

n1 = int(input("Enter n1 number: "))
n2 = int(input("Enter n2 number: "))
n3 = int(input("Enter n3 number: "))
if n1> n2 and n1 > n3:
    print("The n1 greatest number is: ", n1)
elif n2 > n1 and n2 > n3:
    print("The n2 greatest number is: ", n2)
elif n3 > n1 and n3 > n2:
    print("The n3 greatest number is: ", n3)
