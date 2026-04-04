#function is a self contained 


# 2 types of functions:-
# 1. built in function - function is already present inside of python library we can say eg:- type(), input(), print(), eval().
# 2. user define function - according to program requirement programmer can developed the function this is called user defined function.
# def function_name(parameter): - mandatory
#return value - optional


# def msg(): #called function
#     print("hello world!")
# msg () # calling fumction
# msg()


# def arithmatic():
#     a = int(input("Enter the value of A:"))
#     b = int(input("Enter the value of B:"))
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div

# #print(arithmatic()) #calling function
# result = arithmatic()
# print("Arithmati=" , result)




# how many types of arguments we can pass in function
#1. positional argument 
#2. keyword argument
# 3. default argumet
# 4. variable number of argumet/ variable length argumet

#positional argument
# def login(username, password):
#     if username == password:
#         print("login successfully")
#     else :
#         print("invalid credential")
#     pass
# username = input("Enter username:")
# password = input("Enter password:")
# login(username, password)


# # keyword argument
# def login(username, password):
#     if username == password:
#         print("login successfully")
#     else :
#         print("invalid credential")
# login(username = "admin", password = "admin")

#default argument
# def cityname(city = "Goa"):
#     print(city)

# cityname("Delhi")
# cityname("Nagpur")
# cityname()

# #variable length argument/ variable number of argument
# def nameOfCitys(*city):
#     print("City Names:", city)

# nameOfCitys("Goa", "Nagpur", "Pune", "Nashik")


#wap for menu driven code
# import sys
# def add():
#     val1 = int(input("Enter the value of val1: "))
#     val2 = int(input("Enter the value of val2: "))
#     print("Add=", val1+val2)

# def sub():
#     val1 = int(input("Enter the value of val1: "))
#     val2 = int(input("Enter the value of val2: "))
#     print("sub=", val1-val2)

# def mul():
#     val1 = int(input("Enter the value of val1: "))
#     val2 = int(input("Enter the value of val2: "))
#     print("mul=", val1*val2)

# def div():
#     val1 = int(input("Enter the value of val1: "))
#     val2 = int(input("Enter the value of val2: "))
#     print("div=", val1/val2)

# while True:
#     print("1. Add")
#     print("2. subtract ")
#     print("3. multiply")
#     print("4. divide")
#     print("5. exit")
#     choice = int(input("Enter your choice:"))
#     if choice == 1:
#         add()
#     elif choice ==2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:
#         sys.exit()


# 1. rstrip()===>To remove spaces at right hand side
# 2. lstrip()===>To remove spaces at left hand side
# 3. strip()===>To remove spaces at both sides

# programming = input("Enter your programming Name:")
# p_name = programming.rstrip()
# if p_name == "Python":
#     print(p_name)
# elif p_name == "Java":
#     print(p_name)
# elif p_name == "Cpp":
#     print(p_name)
# else:
#     print("Wrong programming name")