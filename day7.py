# mydict = {"C":3, "B":2, "A":1}
# # Sort by key ascending
# print(dict(sorted(mydict.items())))
# # Sort by key descending
# print(dict(sorted(mydict.items(), reverse=True)))




# import sys
# class Queue:
#     def __init__(self, queueSize):  # parameter size constructor
#         self.queueList = []   # queue created
#         self.queueSize = queueSize
#     def isFull(self):
#         if len(self.queueList) == self.queueSize:
#             return True
#         else:
#             return False
#     def Enqueue(self, value):  # add element in queue from rear
#         if self.isFull():
#             print("Queue is Full!")
#         else:
#             self.queueList.append(value)
#     def diaplayQueue(self):
#         print("--------------------------")
#         print(self.queueList)
#         print("--------------------------")
#     def isEmpty(self):
#         if self.queueList == []:
#             return True
#         else:
#             return False
#     def Dequeue(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         else:
#             return self.queueList.pop(0)
#     def DeleteQueue(self):
#         self.queueList = []
#         return "Queue is deleted!"
#     def peek(self):  # returns first element of queue
#         if self.isEmpty():
#             return "Queue is empty"
#         else:
#             return self.queueList[0]
# # main program
# size = int(input("Enter size of Queue: "))
# queueObj = Queue(size)  # Queue object created
# while True:
#     print("\n1. Enqueue Element in Queue")
#     print("2. Display Queue element")
#     print("3. Check isEmpty")
#     print("4. Dequeue element from queue")
#     print("5. Delete queue")
#     print("6. Peek operation")
#     print("7. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         val = int(input("Enter the value for Queue: "))
#         queueObj.Enqueue(val)
#     elif choice == 2:
#         queueObj.diaplayQueue()
#     elif choice == 3:
#         print(queueObj.isEmpty())
#     elif choice == 4:
#         print(queueObj.Dequeue())
#     elif choice == 5:
#         print(queueObj.DeleteQueue())
#     elif choice == 6:
#         print(queueObj.peek())
#     elif choice == 7:
#         sys.exit()



# O(1) - constant time - it takes constant time to access first element
# O(N) - Linera time - linear time since it is visiting every element of array
# O(LogN) - Logarithmic time - logarithmic time since it is visiting only some elements , find an element in sorted array
# O(N^2)- Quadratic - looking array a every index in the array twice
# O(2^N)- Exponential time - double recursion in fibonacci
# stack is using list:-
#       easy to implement
#       speed problem when it grows
# stack usin linked list:-
#        fast performance
#        implementation is not easy.

# def findBiggestNumber(array):
#     firstValue = array[0]
#     for i in range(1, len(array)):
#         if array[i] > firstValue:
#             firstValue = array[i]
#     return firstValue        
# array = [2,4,5,6,7,1,9,3,4,5]
# print(findBiggestNumber(array))


# time complexity: O(1) + O(n)+O(n) = O(n)



# def count_special_and_spaces(message):
#     special_count = 0
#     space_count = 0

#     for ch in message:
#         if ch == " ":
#             space_count += 1
#         elif not ch.isalnum():  # checks special characters
#             special_count += 1

#     return special_count, space_count


# # Input
# msg = input("Enter the message: ")

# # Function call
# special, spaces = count_special_and_spaces(msg)

# # Output
# print("Special Characters:", special)
# print("Spaces:", spaces)



# import math
# n = int(input("Enter number of plots: "))
# areas = list(map(int, input("Enter plot areas: ").split()))
# count = 0
# for area in areas:
#     root = int(math.sqrt(area))
#     if root * root == area:
#         count += 1
# print("Number of square plots:", count)


# def linearSearch(array,target):
#     for i in range(len(array)):     #============>O(n)
#         if array[i]==target:     #===========>O(1)
#             return i             #===========>O(1)
#     return -1                   #===========>O(1)

# array=[1,2,3,4,5,6,7,8,9]
# target=55             # 4 we have to search
# result=linearSearch(array,target)
# if result==-1:
#     print("Not found")
# else:
#     print("Elements found at index no=",result)



#Binary Search
#Binary  search is faster that linear search
#Works only for sorted array
# def binarySearch(array,target):
#     # mid=len(array)//2
#     start=0
#     end=len(array)-1
#     while start<=end:
#         mid=(start+end)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]<target:
#             start=mid+1
#         else:
#             end=mid-1    
#     return -1

# sorted_array=[1,2,3,4,5,6,7,8,9,10]
# target=9
# result=binarySearch(sorted_array,target)
# if result==-1:
#     print("Element not found")
# else:
#     print("Element fount at index=",result)




# WAP Binary Search Algorithm

# def binarySearch(array, target):                            #Time Complexity = O(1)
#     low = 0                                                 #Time Complexity = O(1)
#     high = len(array) - 1                                   #Time Complexity = O(1)

#     while low <= high:                                      #Time Complexity = O(log n)
#         mid = (low + high) // 2                             #Time Complexity = O(1)

#         if array[mid] == target:                            #Time Complexity = O(1)
#             return mid                                      #Time Complexity = O(1)

#         elif array[mid] < target:                           #Time Complexity = O(1)
#             low = mid + 1                                   #Time Complexity = O(1)

#         else:                                               #Time Complexity = O(1)
#             high = mid - 1                                  #Time Complexity = O(1)

#     return -1                                               #Time Complexity = O(1)


# array = [1,2,3,4,5,6,7,8,9]
# target = 4
# result = binarySearch(array, target)                        #Time Complexity = O(log n)

# if result != -1:                                            #Time Complexity = O(1)
#     print("Element found at index", result)                 #Time Complexity = O(1)
# else:
#     print("Element not found")







# WAP to check element in the array using linear search algorithm

# array = [1,2,3,4,5,6,7,8,9]
# target = 4

# def linearSearch(array,target):                                             # Time Complexity = O(1)
#     for i in range(len(array)):                                             # Time Complexity = O(n)
#         if array[i] == target:                                              # Time Complexity = O(1)
#             return i                                                        # Time Complexity = O(1)
#     return -1                                                               # Time Complexity = O(1)

# result = linearSearch(array,target)                                         

# if result != -1:                                                            
#     print("Element found at index",result)                                  
# else:
#     print("Element not found")




# WAP to find the square plot of a given area

# n = int(input("Enter the number : "))
# areas = list(map(int, input("Enter the areas : ").split()))

# count = 0

# for num in areas:
#     i = 1
#     while i * i <= num:
#         if i * i == num:
#             count += 1
#             break
#         i += 1

# print(count)




# WAP give the count of special characters and whitespaces in the input so it is easy to decode the msg

# a = input("Enter a msg : ")
# count = 0

# for i in a:
#     if not i.isalnum():
#         count += 1
# print("\nNumber of special characters and whitespaces : ",count)





# def linearSearch(array, target): #[1,2,3,4,5,6,7,8,9]
#     for i in range(len(array)): #i=3
#         if array[i] == target: #4 == 4
#             return i #=======================================>O(1)
#     return -1 #==============================================>O(1)

# array=[1,2,3,4,5,6,7,8,9]
# target = 55 # 4 we have to search 
# result = linearSearch(array, target)
# if result == -1:
#     print("not found")
# else:
#     print("element found at index no =",result)






class Node:
    def __init__(self,data):
        self.data = data  #instance var
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
linkedlist = LinkedList()

linkedlist.head = Node(5)
second          = Node(10)
Third           = Node(15)
Fourth          = Node(20
                       )
#linking part
linkedlist.head.next = second
second.next = Third
Third.next = Fourth

#Display linkedlist
while linkedlist.head != None:
    print("|",linkedlist.head.data, "|",linkedlist.head.next, "->",end = " ")
    linkedlist.head = linkedlist.head.next