# mydict = {
#     101 : "Prashant",
#     102 : "Ashish",
#     "103" : "Mohini",
#     "104" : "Trivani",
#     101 : "Ashish",
#     102 : "Ashish",
# }
# print(mydict)


#############---------------------------------------------------------------------------------------------------

#with the help of key we have to print values
# a= mydict[102]
# print(a)

####################-----------------------------------------------------------------------------------------------

#we will replace old value by new value
# mydict[102] = "Peter"
# print(mydict)

#######################-----------------------------------------------------------------------------------------------

# only print the keys x=0,1
# for x in mydict:
#     print(x)

####################---------------------------------------------------------------------------------------------

#only print the values
# for x in mydict.values():
#     print(x)

###################---------------------------------------------------------------------------------------------------

#printing key and values both
# for x ,y in mydict.items():
#     print(x,y)

#####################-------------------------------------------------------------------------------------------------

#if i have to add new key and value pair in my dictionary 
# mydict["mobile_no"] = 4455661122
# print(mydict)

########-------------------------------------------------------------------------------------------------------------------

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

##########-----------------------------------------------------------------------------------------------------

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])

##########-------------------------------------------------------------------------------------------------------

# arr = {}
# arr[1] = 1 #arr{1:1 , '1':2} = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0   #4
# for k in arr:  #k=0:
#     sum += arr[k]
# print(sum)

#########################3-------------------------------------------------------------------------------------------------------------


# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)

#########-----------------------------------------------------------------------------------------------------------------------------

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict) 

##############----------------------------------------------------------------------------------------------------

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box    
# crates['jars'] = jars
# print(len(crates[box]))

##################---------------------------------------------------------------------------------------------------------

# dict = {'c':97,'a':96,'b':98}
# for _ in sorted (dict):
#     print (dict[_])

################----------------------------------------------------------------------------------------------------------------------

# rec = {"Name": "Python", "Age":"20"}
# r = rec.copy()
# print(id(r))
# print (id(rec))  # False, because r is a new dictionary

##############------------------------------------------------------------------------------------------------------------------------

# rec = {"Name": "Python", "Age":"20", "Addr": "N3", "Country": "USA"}
# id1 = id(rec)
# del rec
# rec = {"Name": "Python", "Age":"20", "Addr": "N3", "Country": "USA"}
# id2 = id(rec)
# print(id1 == id2)  # False, because the original dictionary was deleted and a

#############################------------------------------------------------------------------------------------------------------------------

# Find the key with the minimum value in a dictionary
# Q. Write a function to find the key with the minimum value in a dictionary
#Input : {"X" : 20, "Y" : 10, "Z" : 30}
#Output : "Y"

# def min_key(d):
#     return min(d, key=d.get)

# data = {"X": 20, "Y": 10, "Z": 30}

# result = min_key(data)
# print(result)

##########################----------------------------------------------------------------------------------------------------------------

# mydict = {
#     101 : "Prashant",
#     "Professional" : "Developer",
#     "empid" : 1001
# }

# mydict.pop(101)
# print(mydict)

#################--------------------------------------------------------------------------------------------------------------------------------

#Nested for loop:

#for i in range():==>outer loop==> Row's
        #   for j in range():==>inner loop==> Col's
                     #print(i, end = " ")
             #print()
             
# for i in range(1,4): #==>outer loop==> Rows
#     for j in range(1,4):# ==>inner loop==> Cols 
#                      print(i, end = "  ")
#     print()
             

#############----------------------------------------------------------------------------------------------------------

# n=int(input("Enter the number of rows: ")) #n=5
# for i in range(1,n+1): #==>outer loop==> Rows
#     for j in range(1,i+1):# ==>inner loop==> Cols 
#                      print(j, end = "  ")
#     print()

####################################---------------------------------------------------------------------------------------------------

# n=int(input("Enter the number of rows: ")) #n=5
# for i in range(1,n+1): #==>outer loop==> Rows
#     for j in range(1,i+1):# ==>inner loop==> Cols 
#                      print(chr(64+i), end = "  ")
#     print()

#######-----------------------------------------------------------------------------------------------------------------------------------

# n=int(input("Enter the number of rows: ")) #n=5
# for i in range(1,n+1): #==>outer loop==> Rows
#     for j in range(1,n+2-i):# ==>inner loop==> Cols 
#                      print("*", end = "  ")
#     print()

###############---------------------------------------------------------------------------------------------------------

# n=int(input("Enter the number of rows: ")) #n=5
# for i in range(1,n+1): #==>outer loop==> Rows
#     for j in range(1,n+2-i):# ==>inner loop==> Cols 
#                      print(chr(64+j), end = "  ")
#     print()

########-------------------------------------------------------------------------------------------------------

# import time 
# n=int(input("Enter the number of rows: ")) #n=5
# for i in range(1,n+1): #==>outer loop==> Rows
#     for j in range(1,n+2-i):
#         time.sleep(2)
#         print(n+1-i, end = "  ")
#     print()

#######----------------------------------------------------------------------------------------------------------------------
# import time
# n=int(input("Enter the number of rows: ")) #n=5
# for i in range(1,n+1): #==>outer loop==> Rows
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):# ==>inner loop==> Cols 
#             time.sleep(2)
#             print("*", end = "  ")
#     print()
