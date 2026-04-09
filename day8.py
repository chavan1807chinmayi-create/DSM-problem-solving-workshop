# # Number of days (M) and products (N)
# M, N = 3, 4
# # Sales data (each row = one day)
# sales = [
#     [100, 198, 333, 323],
#     [122, 232, 221, 111],
#     [223, 565, 245, 764]
# ]
# # Find and print maximum revenue for each day
# for i in range(M):
#     max_value = sales[i][0]   # assume first value is max
#     for j in range(N):
#         if sales[i][j] > max_value:
#             max_value = sales[i][j]
#     print(max_value, end=" ")




# import sys

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class  LinkedList:
#     def __init__(self):
#         self.head = None

#     def addnode(self, value):
#         new_node = node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
    
#     def addNodeinBeginning(self, value):
#         new_node = node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def addNodeinBetween(self, value, left_value, right_value):
#         if self.head is None:
#             print("List is empty. Cannot insert between nodes.")
#             return

#         current = self.head
#         while current is not None:
#             if current.data == left_value and current.next is not None and current.next.data == right_value:
#                 new_node = node(value)
#                 new_node.next = current.next
#                 current.next = new_node
#                 if current is self.tail:
#                     self.tail = new_node
#                 return
#             current = current.next

#         print(f"No adjacent nodes found with values {left_value} and {right_value}. Cannot insert {value} between them.")

#     def addNodeatEnd(self, value):
#         new_node = node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

#     def display(self):
#         current = self.head
#         while current is not None:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

#     def exit(self):
#         sys.exit()








# if __name__ == "__main__":
#     obj = LinkedList()

#     while True:
#         print("\n1. Add Node in Linked List :")
#         print("2. Add node in Beginning :")
#         print("3. Add node Between  :")
#         print("4. Add node at End :")
#         print("5. Display Linked List :")
#         print("6. Exit")
        
#         choice = int(input("Enter your choice : "))
        
#         if choice == 1:
#             val = int(input("Enter value for node : "))
#             obj.addnode(val)
#         elif choice == 2:
#             val = int(input("Enter value for node : "))
#             obj.addNodeinBeginning(val)
#         elif choice == 3:
#             val = int(input("Enter value for node : "))
#             left_val = int(input("Enter the value of the node before the new node: "))
#             right_val = int(input("Enter the value of the node after the new node: "))
#             obj.addNodeinBetween(val, left_val, right_val)
#             print("Element Added Successfully")
#         elif choice == 4:
#             val = int(input("Enter value for node : "))
#             obj.addNodeatEnd(val)
#         elif choice == 5:
#             obj.display()
#         elif choice == 6:
#             obj.exit()





# import sys
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def AddNode(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node

#     def display(self):
#         current = self.head
#         if current is None:
#             print("Linked list is empty")
#             return
#         while current:
#             print("|", current.data, "|", end=" -> ")
#             current = current.next
#         print("None")
        
#     def addNodeBeginning(self,value):
#         node = Node(value)  
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             node.next = self.head
#             self.head = node

#     def AddInBetween(self,index, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         elif index == 0:
#             node.next = self.head
#             self.head = node
#         else:
#             temp = self.head
#             for _ in range(index-1):
#                 temp = temp.next
#             node.next = temp.next
#             temp.next = node       

#     def AddAtEnd(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node    
    
# linkedlist = Linkedlist()

# if __name__ == "__main__":
#     object = Linkedlist()

#     while True:
#         print("1.Add node in linked list: ")
#         print("2.Add node at beginning: ")
#         print("3.Add node in between: ")
#         print("4.Add node at end: ")
#         print("5.Display linked list: ")
#         print("6.Exit: ")

#         choice = int(input("enter your choice: "))

#         if choice == 1:
#             value = int(input("enter value here: "))
#             object.AddNode(value)
#             print("Node added successfully")

#         elif choice == 2:
#             value = int(input("enter value here: "))
#             object.addNodeBeginning(value)

#         elif choice == 3:
#             value = int(input("enter value add node in between: "))
#             index = int(input("enter position after you have to insert: "))
#             object.AddInBetween(index,value)   
#             print("Add successfully")

#         elif choice == 4:
#             value = int(input("enter value here: "))
#             object.AddAtEnd(value)   

#         elif choice == 5:
#             object.display()

#         else:
#             sys.exit()




# import sys
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None


#     def AddNode(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self. tail = node


#     def display(self):
        
#         current = self.head  #temp pointing
#         if current is None:
#             print("Linked list is empty")
#             return
#         while current:
            
#             print("|", current.data, "|", end=" -> ")
#             current = current.next
        
#         print("None")
                
#     def AddAtbeginning(self, value) :
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             node.next = self.head
#             self.head = node   


#     def AddInBetween(self, value, pos):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node

#         elif pos == 0:
#             node.next = self.head
#             self.head = node

#         else:
#             temp = self.head
#             for i in range(pos-1):
#                 temp = temp.next

#             node.next =  temp.next
#             temp.next = node         



#     def deleteNode(self,  index):
#         if self.head is None:
#             print("Linked list is empty..")
#             return

#         if index == 0:
#             self.head = self.head.next

            
       
    
        

#     def AddAtEnd(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node

#         else:
#             self.tail.next = node
#             self.tail = node    



# if __name__ == "__main__":
#     object = Linkedlist()

#     while True:
#         print("1.Add node in linked list: ")
#         print("2.Add node at beginning: ")
#         print("3.Add node in between: ")
#         print("4.Add node at end: ")
#         print("5.Display linked list: ")
#         print("6. Delete node ")
#         print("7.Exit: ")

#         choice = int(input("enter your choice: "))

#         if choice == 1:
#             value = int(input("enter value here: "))
#             object.AddNode(value)
        

#         elif choice == 2:
#             value = int(input("enter value here: "))
#             object.AddAtbeginning(value)

#         elif choice == 3:
#             value = int(input("enter value here: "))
#             pos = int(input("enter position :"))
#             object.AddInBetween(value, pos)


#         elif choice == 4:
#             value = int(input("enter value here"))
#             object.AddAtEnd(value)   

#         elif choice == 5:
#             object.display()


#         elif choice == 6:
#             index = int(input("enter index of node: "))
#             object.deleteNode(index)    

#         else:
#             sys.exit()







# write a function to remove leading zaros from a list of integers.
# A = [0,0,  2, 5, 0, 1]  
# while A[0] == 0:
#     A.pop(0)
# print(A)

# regular expression :-
#compile() function
# import re #
# count = 0
# pattern = re.compile("function")
# #print(pattern)
# matcher = pattern.finditer("Python is a versatile and widely-used programming language known for its simplicity and readability. It supports multiple programming paradigms, including object-oriented, procedural, and functional programming. Python is popular in fields like web development, data science, artificial intelligence, and automation due to its extensive libraries and frameworks. Its large community and easy-to-learn syntax make it an ideal choice for both beginners and experienced developers.")
# #print(matcher)
# for i in matcher:
#     count += 1
#     print(i.start(),"....",i.group())
# print("The number of occurances: ",count)
# 
# ===============================================================================================
# import re
# count = 0 
# matcher = re.finditer("Hi","HiHiHiHiHi")   
# #print(matcher)
# for i in matcher: #loop 4 times execute HiHiHiHi
#     count += 1
#     print(i.start(),"....",i.end(),"....",i.group()) 
# print("The number of occurences:",count)





# import re
# obj=input("enter any character:")
# objmatch=re.finditer(obj,"a7b @k29z")
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())




# match() function operation
# import re
# a = input("Enter string to perform match operation: ")
# mtch = re.match(a, "python is very import languge")
# print (mtch)
# if mtch!= None:
#     print("match fount at beginning level")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("There is no matching at beginning level")






# fullmatch()
# import re
# a = input("Enter string to perform match operation: ")
# mtch = re.fullmatch(a, "pythonisvery")
# print(mtch)
# if mtch!= None:
#     print("match found")
#     print(mtch.start(), " ", mtch.end())
# else:
    # print("There is no matching at beginning level")




# serach()
# if the match found anywhere in the string then it return object else it will return None 




# import re
# a = input("Enter string to perform match operation: ")
# f = open('myhope.txt','r')
# c = f.read()
# mtch = re.search(a, c)
# print(mtch)
# if mtch!=None:
#     print("Match found at begining level ")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("There is no matching at beginning level")







# findall()
# this function return  a list which constraint 
# import re
# mtch = re.findall('[a-zA-Z0-9]',"abch2hdhyhvfbe7774888wf88w9")
# print(mtch)

# sub()
# this function perform substitution or replacement
#re.sub(expression, replacement, string) here every match pattern will be replaced by provided replacement
# import re
# obj = re.sub('[a-zA-Z]','X','2345 ABCD Fabc deff')
# print(obj)



# subn()
#it is as similar as sub() function only one thing is different that it also return number of replacement. This return in tuple where first elements is string and second one of replacement.











# split()
# this function is used to split the given string as per the some pattern then we should use split() function.
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# count = len(words)
# print("Total words:", count)













# wap to check the valid mobile number
# import re
# no = input("Enter mobile number: ")
# obj = re.fullmatch("[6-9]\d{9}", no)
# if obj is not None:
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")





# import re
# email = input("Enter email: ").strip()
# pattern = r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}"
# obj = re.fullmatch(pattern, email)
# if obj is not None:
#     print("Valid email")
# else:
#     print("Invalid email")



# import re
# email = input("Enter email: ")
# pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"
# obj = re.fullmatch(pattern, email)
# if obj is not None:
#     print("Valid email")
# else:
#     print("Invalid email")



# import re
# email = input("Enter email: ")
# pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+(\.[a-zA-Z]{2,})+"
# obj = re.fullmatch(pattern, email)
# if obj is not None:
#     print("Valid email")
# else:
#     print("Invalid email")







# import os,sys
# fname = input("Enter File Name: ")
# if os.path.isfile(fname):
#     print("File exist:", fname)
#     f = open(fname, "r")
# else:
#     print("File does not exist:", fname)
#     sys.exit(0)
# print("The content of file is:")
# data = f.read()
# print(data)