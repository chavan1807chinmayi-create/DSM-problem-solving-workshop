#write a function to reverse the order of element in a list.
# my_list = [1, 2, 3, 4, 5]
# reversed_list = my_list[::-1]
# print(reversed_list)

#write a function to check if a list is a palindrome.
# my_list = [1, 2, 3, 2, 1]
# if my_list == my_list[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# write a function to find common elements between two lists.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# result = []
# for i in list1:
#     if i in list2:
#         result.append(i)
# print(result)

# python object oriented programming 
#class in python 
# class Student:
#     roll_no = 101
#     def studentData(self): #menthod function or member function
#         print("Student information")

# obj = Student()
# print(obj.roll_no)
# obj.studentData()

# class Demo:
#     def __init__(self):
#         print("I am constructor:")
#     def msg(self):
#         print("Hello class!")
# obj1 = Demo()
# # print(obj1)
# obj2 = Demo()
# obj1.msg() #constructor use to create memory and default address


# class Hod:
#     def __init__(self):
#         self.name = 'chinamyi chavan'
#         self.age=20
#         self.empid=1001
#     def info(self):
#         print("My name is:",self.name)
#         print("My age is:",self.age)
#         print("My emp id: ",self.empid)
# obj= Hod()
# obj.info()


# class Hod:
#     def __init__(self,name,age,rollno):
#         self.name = name
#         self.age= age
#         self.rollno = rollno
#     def show(self):
#         print("name ",self.name)
#         print("age:",self.age)
#         print("rollno: ",self.rollno)
# obj= Hod('Arjun',24,101)
# obj.show()




# class New:
#     def __init__(self):
#         self.a = 10
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)
# Obj1.a = 20
# print()
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)


# class Student:
#     def __init__(self):
#         self.s_name = "chinmayi"
#         self.s_rollno = 101    #decalring a instance var inside a constructor

#     def getdata(self):
#         self.s_mb = 8989899888   #decalring the instance var inside a instance method
# obj = Student()
# obj.getdata()
# del obj.s_mb     #delete the instance variable using obj
# obj.s_branch = "CE"    #adding instance variable by using object
# print(obj.__dict__)


# class New:
#     a = 10
#     def __init__(self):
#         self.name="chinmayi"
        
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a = 50
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)



# import sys
# class Student:
#     def __init__(self):
#         self.students = []
#     def add_student(self):
#         roll = input("Enter Roll Number: ")
#         name = input("Enter Student Name: ")
#         city = input("Enter Student City: ")
#         sid = input("Enter Student ID: ")
#         # prevent duplicate ID
#         for s in self.students:
#             if s[3] == sid:
#                 print("ID already exists!")
#                 return
#         self.students.append([roll, name, city, sid])
#         print("Student Added!")
#     def show_student(self):
#         if not self.students:
#             print("No Data Found")
#             return

#         print("\n{:<10}{:<20}{:<20}{:<15}".format("Roll", "Name", "City", "ID"))
#         print("-"*65)
#         for s in self.students:
#             print("{:<10}{:<20}{:<20}{:<15}".format(s[0], s[1], s[2], s[3]))

#     def update_student(self):
#         sid = input("Enter Student ID to Update: ")
#         for s in self.students:
#             if s[3] == sid:
#                 s[0] = input("Enter New Roll Number: ")
#                 s[1] = input("Enter New Name: ")
#                 s[2] = input("Enter New City: ")
#                 print("Updated Successfully!")
#                 return
#         print("Student Not Found")

#     def delete_student(self):
#         sid = input("Enter Student ID to Delete: ")
#         for s in self.students:
#             if s[3] == sid:
#                 self.students.remove(s)
#                 print("Deleted Successfully!")
#                 return
#         print("Student Not Found")


# obj = Student()

# while True:
#     print("\n1.Add Student")
#     print("2.Show Student")
#     print("3.Update Student")
#     print("4.Delete Student")
#     print("5.Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         obj.add_student()
#     elif choice == 2:
#         obj.show_student()
#     elif choice == 3:
#         obj.update_student()
#     elif choice == 4:
#         obj.delete_student()
#     elif choice == 5:
#         print("Program Closed")
#         sys.exit()



# class Student:
#     def __init__(self, name , rollno, mob):
#         self.name = name
#         self.rollno = rollno
#         self.mob = mob

#     def display(self):
#         print(self.name," ",self.rollno, " ", self.mob)

# stud = Student("Chinmayi", 100, 5656565656)
# stud.display()



#static method - we can static method when the code that belongs to class it do not use the object.
# we will not use any instance or class variable
# they are not dependent on the state of the object
# we can declare static method using @staticmethod

# class Student:
#     # by using class name we can access static method
#     @staticmethod 
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail =",firstname,lastname)

#     @staticmethod
#     def contact_detail(mobile_no, rollno):
#             print("your contact detail = ",mobile_no,rollno)

# Student.get_personal_detail("Chinmayi","Chavan")
# Student.contact_detail(6767676778, 1001)



# class College:
#     def college_name(self):
#         print("Modern college")


# class Student(College):
#     def student_info(self):
#         print("Name: Prashant Jha")
#         print("Branch: Mechanical")


# obj = Student()
# obj.college_name()
# obj.student_info()




# 2.Multilevel Inheritance
# class College: #Parent Class
#     def college_name(self): 
#         print("Modern College")
# class Student(College): #Child Class
#     def student_name(self): #Member Function
#         print("Student Name: Om Retharekar")
#         print("Branch: Computer Science")
# class Exam(Student): #Child Class
#     def subjects(self):
#         print("Subject1: Maths")
#         print("Subject2: Physics")
#         print("Subject3: Chemistry")
# obj = Exam()
# obj.college_name()
# obj.student_name()
# obj.subjects()



# class SubMarks:
#     math = int(input("Enter paper marks of maths: "))
#     DE = int(input("Enter paper marks of design engineering: "))
#     C = int(input("Enter paper marks of c language: "))
#     english = int(input("Enter paper marks of english: "))

# class PrcatMarks:
#     cpract = int(input("Enter practicals marks of c language: "))

# class Result(SubMarks, PrcatMarks):
#     # print("if student pass in both = subject and practical paper then pass")
#     def total(self):
#         if self.math>= 40 and self.DE >= 40 and self.c >= 40 and self.english >= 40 and self.cpract>=20:
#             print("pass")
#         else:
#             print("fail")
# obj = Result()
# obj.total()




# polymorphism example
# class Principal:
#     def role(self):
#         print("i am manage all activity of college")

# class Dean:
#     def role(self):
#         print('Dean = i am decision taking person')

# class Hod:
#     def role(self):
#         print('Hod = i am manage all activity of department')

# class Faculty:
#     def role(self):
#         print('Faculty = i am teach students')

# def func(obj):
#     obj.role()
# campus= [Principal(),Dean(),Hod(),Faculty()]
# for obj in campus:
#     func(obj)




# python does not support method/ function overloading  and construction overloading
# if we are trying to declare multiple methods with same name and different number of argument then python will always consider only 1.

# class Arithmetic:
#     def add(self,a):
#         print (a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c ):
#         print (a+b+c)
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)



# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None:
#             print(a+b)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         else:
#             print("enter atleast two argument")
# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)




# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None:
#             print(a+b)
#         elif a!=None and b!=None:
#             print(a+b+c)
#         else:
#             print("Enter at least two numbers")
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)




# class Arithmatic:
#     def __init__(self):
#         print("There is no argument")
#     def __init__(self,a):
#         print("Passing one argument")
#     def __init__(self,a,b):
#         print("Passing two argument")

# obj =Arithmatic()
# obj = Arithmatic(10)
# obj = Arithmatic(2,2)


# Method overloading means defining a method with the same name but different number or type of parameters.
# Python does not support true method overloading. It is achieved using:
# default arguments
# variable arguments (*args)

# Method overriding means redefining a method in the child class that already exists in the parent class.
# Overloading: same method name, different parameters
# Overriding: same method name, but child class changes behavior

# #method overriding(parent and child relationship must be there)
# class Rbi:
#     def home_loan(self):
#         print("Home loan = 7.5")
#     def carloan(self):
#         print("Car loan 8% ")

# class Sbi(Rbi):
#     def home_loan(self):
#         print("Sbi Provide home loan = 6.5")
# obj = Sbi()
# obj.home_loan() # child class method override the parent class method


# #method overriding(parent and child relationship must be there)
# class Rbi:
#     def home_loan(self):
#         print("Home loan = 7.5")
#     def carloan(self):
#         print("Car loan 8% ")

# class Sbi(Rbi):
#     def home_loan(self):
#         print("Sbi Provide home loan = 6.5")
#         super().home_loan() #using super() we can access parent class method into the child class
# obj = Sbi()
# obj.home_loan() # child class method override the parent class method



# class Father:
#     def __init__(self):
#         print("Father := i am allready at breakfast table")

# class child(Father):
#     def __init__(self):
#         super().__init__()
#         print("Child := i am coming to breakfast table")

# obj = child()



