# ctrl + shift + e = file explore 

# print('chinmayichavan1807'.isalnum())
# print('chinmayichavan'.isalpha())
# print('188f'.isdigit())
# print('sdssfsd'.islower())
# print(' '.islower())
# print('CHINMAYI'.upper())
# print('My Name Is Chinmayi'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("hello".endswith("lo"))


# print("Chinmayi".find("i")) # if any other element wants to find then it will be give us -1 
# print("Chinmayi".index("n"))
# print("chinmayi chavan".count("a"))


#write a function to check if a key exits in a dictionary.
# def check_key(d, key):
#     if key in d:
#         return True
#     else:
#         return False
# my_dict = {"a": 1, "b": 2, "c": 3}

# key = input("Enter key to check: ")

# if check_key(my_dict, key):
#     print("Key exists in dictionary")
# else:
#     print("Key does not exist in dictionary")





# # write a function to count the frequency of elemements in a list using a dictionary.
# def count_frequency(lst):
#     freq = {}
#     for i in lst:
#         freq[i] = freq.get(i, 0) + 1
#     return freq

# my_list = [1, 2, 2, 3, 3, 3, 4]

# print(count_frequency(my_list))


#exception handling  also known as runtime error.
# pre-defined and user-defined exception 
# class should be in 1st letter Capital
# exception handling by try and except

# n1 = int(input("Enter first value: "))
# n2 = int(input("Enter second value: "))
# try:
#     print(n1/n2)
# except:
#     print("Can't divide by zero baby !")

# print("To be continue babe!")


# we can handle multiple exception with multiple exception block 
# try:
#     n1 = int(input("Enter first value: "))
#     n2 = int(input("Enter second value: "))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("Can't divide by zero baby !")
# except ValueError:
#     print("Enter only integer value!")
# print("To be continue babe!")



#handling multiple different kinds of execption with single except block.
# try:
#     a = int(input("Enter first interger no"))
#     b = int(input("Enter second interger no"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)
# print("to be continue!")




# # the concept of default except block , generaly we used 
# try:
#     a = int(input("Enter first interger no"))
#     b = int(input("Enter second interger no"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number: ", message)
# except:
#     print("this is default part of except block!")



# we can use else block if no error will generate it is 
# try:
#     a = int(input("Enter first interger no"))
#     b = int(input("Enter second interger no"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number: ", message)
# else:
#     print("Everything is ok!")



#finally block will always executed whether try block generate error or not
# try:
#     a = int(input("Enter first interger no"))
#     b = int(input("Enter second interger no"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number: ", message)
# finally:
#     print("i will allways excuted!")


# nested try except block 

# try:
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second number: "))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#         print(msg)


# try:
#     a = int(input("Enter first number"))
#     b = int(input("Enter second number"))
#     print(a/b)
# except (ZeroDivisionError , ValueError)as msg:
#         print(msg)
# else:
#     print("there are no error in try block ,Everything is ok")
# finally:
#     print("i am finally block , I will always executed")

# def security_key(n):
#     s = str(n)
#     for d in set(s):
#         if s.count(d)>1: return d
#     return -1 
# print(security_key(578378923))

# def security_key(n):
#     s = str(n)
#     for i in reversed(s):
#         if s.count(i) > 1:
#             return i
#     return -1
# print(security_key(578378923))


# mylist = [5,7,8,3,7, 8, 9,2,3]
# newlist=[]

# for i in range(len(mylist)):
#     count = 0
#     key = mylist[i]

#     j = i + 1
#     while j < len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j = j + 1
# print(len(newlist))


# find 2nd largest element
# list = [7, 3, 9, 2, 8]
# list.sort()
# print(list)
# print(list[-2])


#while loop
# i = 1
# while i<=5:
#     print(i)
#     i = i + 1


# username=""
# password = ""
# while username != "admin" or password != "admin":
#     username = input("Enter username :")
#     password = input("Enter password :")
    

# name = "programming"
# v = 0
# c = 0
# for i in name:
#     if i in "aeiou":
#         v += 1
#     else:
#         c += 1
# print("Vowels:", v)
# print("Consonants:", c)




# name = 'programming'
# vowels = ['a', 'e', 'i', 'o', 'u']
# cons = 0
# vowel = 0
# for i in name:
#     if i in vowels:
#         vowel +=1
#     else:
#         cons+=1
# print("consonants=", cons)
# print("vowels = ", vowel)






#wap a function to remove all occurreneces of a specific element from a list.
# my_list = [1, 2, 3, 2, 4, 2]
# c = 2
# while c in my_list:
#     my_list.remove(c)
# print(my_list)





# wap a function to calculate the product of all elements in a list
# my_list = [2, 3, 4, 5]
# r = 1
# for i in my_list:
#     r *= i
# print(r)


# f = open("mylife.txt","w")
# print("name of file : ", f.name)
# print("file mode    :",f.mode)
# print("readeble     :",f.readable())
# print("writable     :",f.writable())
# print("file.closed  :",f.closed)
# f.close()
# print("file closed:",f.closed)



# performing write operation
# f=open("mylife.txt","a")
# f.write("\n Pune is a smart city!")
# f.write("\n Banglore is a smart city!")
# f.write("\n Nashik is a smart city!")
# f.write("\n goa is a smart city!")
# f.close()
# print("file operation is done")




# inserting list
# f = open("mylife.txt","w")
# mylist =("Chinmayi","Harsha","Mehul","3","18","0")
# f.writelines(mylist)
# f.close()
# print("written work has done succefully!")



#reading data from a file
# f = open("mylife.txt","r")
# print(f.read())
# f.close


# with open("mylife.txt","w") as f:
#     f.write("amit\n")
#     f.write("chinmayi\n")
#     f.write("vighnesh\n")
#     print("file closed:",f.closed)
# print("file closed:",f.closed)



# with open("mylife.txt","r") as f:
#     content = f.read()
#     print(content)

# f1=open("image.jpg","rb")
# f2=open("image2.jpg","wb")
# data = f1.read()
# f2.write(data)
# print("new image is available with the name")




# import csv 
# f = open("student.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["StudentID","Rollno","Name","Mobile No"])
# StudentID = int(input("Enter Student ID:"))
# Rollno = int(input("Enter your roll number"))
# Name = input("Enter your name")
# MobileNo = int(input("Enter you mobile number"))
# a.writerow([StudentID, Rollno, Name, MobileNo])
# print("Student record has save")



import csv

with open("Chinmayi.csv", "a", newline="") as f:
    writer = csv.writer(f)

    rollno = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    mobile = input("Enter Mobile Number: ")

    p1 = int(input("Enter marks of Subject 1: "))
    p2 = int(input("Enter marks of Subject 2: "))
    p3 = int(input("Enter marks of Subject 3: "))

    total = p1 + p2 + p3
    percentage = total / 3

    if p1 >= 40 and p2 >= 40 and p3 >= 40:
        result = "Pass"
    else:
        result = "Fail"

    writer.writerow([rollno, name, mobile, p1, p2, p3, total, percentage, result])

print("Student record saved successfully!")