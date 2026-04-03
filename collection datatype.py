# mylist = ["chinmayi", "Komal", "Vidya", 18, 19, "chinmayi", 88]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[0:3])
# print(mylist[0:5])
# print(mylist[:5])
# print(mylist[3:])
# print(mylist[:])
# print(mylist[0:6:2])
# print(mylist[::2])
# print(mylist[::-1])

# mylist[0] = "chinamyi"
# print(mylist)


# mylist.append("Harsha")
# mylist.append("Baby")
# print(mylist)

# if "chinmayi" in mylist:
#     print("present")
# if "chinmayi" not in mylist:
#     print("not present")

# mylist.insert(2, "Mehul")
# print(mylist) #it will insert "Mehul" at index 2 and shift the rest of the elements to the right

# mylist.remove("chinmayi")
# print(mylist)  #it will remove the first occurrence of "chinmayi" from the list

# mylist.pop()
# print(mylist) #it will remove the last element of the list

# newlist = mylist.copy()
# print(newlist) #it will create a new list with the same elements as mylist

# mylist = [['chinmayi', 'Komal'], ['19.18'], [ 'chinmayi', 88]]
# print("Example of multidimensional list: ")
# print(mylist)
# # print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])



# list1 = ["Chinmayi","Chavan"]
# print(list1*2)     #it will repeat the list 2 times

# list2 = [1,2,3]
# print(list1+list2)   #it will concatenate the two lists


# list2 = [1,2,3, 'chinmayi']
# del list2[3]
# print(list2)

# list2 = [1,2,3, 'chinmayi']
# list2.clear()
# print(list2) #it will clear the list and make it empty list


# name = "chinmayi"
# print(name)
# myname = list(name)
# print(myname) #it will convert the string into a list of characters or we can say list constructor or list value in single character

#we have used list constructor

# mylist = [18, 19, 22, 27]
# mylist.reverse()
# print(mylist) #it will reverse the list in place

#sorting the list
mylist = [18, 19, 22, 27, 10, 5, 1]
# mylist.sort()
# print(mylist) #it will sort the list in ascending order

# mylist.sort(reverse=True)
# print(mylist) #it will sort the list in descending order

#default sorting order for number is ascending order and for string is alphabetical order
#we should know that list should contain homogenious 
#elements to sort the list otherwise it will give error


#alising the list

#alising means assigning the one variable to another variable and both variables will point to the same list in memory
# mylist = [18, 19, 22, 27, 10, 5, 1]
# newlist = mylist #assigning the address
# print(id(mylist))
# print(id(newlist)) #both variables are pointing to the same list in memory
# mylist[0] = "Chinmayi"
# print(mylist)
# print(newlist) #it will also change the newlist because both variables are pointing to the same list in memory

#here we used id() function to check the memory address of the list and we can see that both mylist and newlist are pointing to the same memory address.



# arr = [[1,2,3,4], 
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]#it is a 2D list or a list of lists
# for i in range(0, 4):#it will iterate through the outer list and print the inner lists
#     print(arr[i].pop()) #it will pop the last element of each sublist and print it

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i - 1] = arr[i]
# for i in range(0, 6):
#     print(arr[i], end = " ") #it will print the elements of the list in a single line with space in between


# fruit_list1= ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Apricot'
# fruit_list3[1] = 'Blueberry'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Apricot':
#         sum += 1
#     if ls[1] == 'Blueberry':
#         sum += 20
# print(sum)




# a = [1, 2, 3, 4, 5, 6, 7, 8, 9] #it is a list of integers from 1 to 9
# a[::2] =10,20,30,40,50,60 #it will replace the elements at index 0,2,4,6,8 with the values 10,20,30,40,50,60 respectively and the rest of the elements will remain unchanged
# print(a) #it will replace the elements at index 0,2,4,6,8 with the values 10,20,30,40,50,60 respectively and the rest of the elements will remain unchanged

# a = [1, 2, 3, 4, 5]
# print(a[3:0:-1]) #it will print the elements from index 3 to index 1 in reverse order

#tuple and list are both collection data types in python but tuple is immutable and list is mutable
#tuple is defined using parentheses () and list is defined using square brackets []
#tuple is faster than list because it is immutable.
#tuple is used when we want to store a collection of items that should not be changed and list is used when we want to store a collection of items that can be changed.
#tuple is hashable and list is unhashable because tuple is immutable and list is mutable.
#tuple can be used as a key in a dictionary and list cannot be used as a key in a dictionary because tuple is hashable and list is unhashable.
#tuple is used to store heterogeneous data and list is used to store homogeneous data but it is not a strict rule and we can store heterogeneous data in a list and homogeneous data in a tuple as well.

# mytuple = ("chinmayi", "komal", "vidya", 18, 19, "chinmayi", 88, "188.8")
# print(mytuple)
# print(type(mytuple))

# mytuple[2] ="sunil" #it will give an error because tuple is immutable and we cannot change the elements of a tuple
# print(mytuple)

# init_tuple=()
# print(init_tuple.__len__())#answer = 0

# init_tuple_a = 'a','b'
# init_tuple_b = ('a','b')
# # print(id(init_tuple_a == init_tuple_b))
# print(init_tuple_a == init_tuple_b)# answer:-true


# init_tuple_a = '1','2'
# init_tuple_b = ('3','4')
# print (init_tuple_a + init_tuple_b)


# init_tuple = ('Python')*3
# print(type(init_tuple))

# init_tuple = ('Python',)*3 
# print(type(init_tuple))


# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)   # answer:- tuple changing not allowed


# init_tuple = ((1,2),)*7 
# print(len(init_tuple[3:8])) #answer:- 4


# names = [4,2,5,6,8,2]
# for i in names: 
#     print(i)


# wap to move zero in the last
# A = [4,0,2,5,0,1]
# for i in A:
#     if i == 0:
#         A.remove(i)
#         A.append(i)
#     print(A)
# B= [4,2,5,1,0,0]

# # ...existing code...
# A = [4, 0, 2, 5, 0, 1]

# non_zero = [x for x in A if x != 0]   # [4,2,5,1]
# count_zero = A.count(0)               # 2
# B = non_zero + [0] * count_zero       # [4,2,5,1,0,0]

# print(B)
# # ...existing code...


# A =[1, 2,2, 3, 4, 4, 5]
# newlist= []
# for i in A:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)



# A = [1, 2, 3], [2, 3, 4], [3, 4, 5]
# # common elements in 2+ lists
# l1 = [1, 2, 3]
# l2 = [2, 3, 4]
# l3 = [3, 4, 5]

# common = set(l1) & set(l2) & set(l3)
# print(common)  # {3}

# # if list tuple A = ([1,2,3], [2,3,4], [3,4,5])
# A = ([1,2,3], [2,3,4], [3,4,5])
# common = set(A[0]).intersection(*A[1:])
# print(common)  # {3}

# A = [1, 2, 3], [2, 3, 4], [3, 4, 5]
# common = set(A[0]).intersection(*A[1:])   # {3}
# print(list(common))                       # [3] (order not guaranteed)
# ...existing code...



# A = [1, 2, 3], [2, 3, 4], [3, 4, 5]
# A = [1, 2, 3]
# B = [2, 3, 4]
# C = [3, 4, 5]
# for i in A:
#     if i in B and i in C:
#         print(i)




# n = int(input("enter size of array:"))
# arr = []
# for i in range(n):
#     val = int(input("enter the value of array:"))
#     arr.append(val)
# sum = 0
# print(arr)
# for i in range(n):
#     if i+1 in range(n):
#         sum += abs(arr[i]- arr[i+1])
#     print(sum) # wrong need to do correct




# n = int(input("enter size of array: "))
# arr = []
# for _ in range(n):
#     arr.append(int(input("enter the value of array: ")))

# total = 0
# for i in range(n - 1):
#     total += abs(arr[i] - arr[i + 1])

# print(arr)
# print("sum of abs diffs:", total)




# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)


# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

#zip() inside we can take multiple range function
# for i, j in zip(range(1,6), range(5,0,-1)):
#     if i == 3 and j ==3:
#         continue 
#     print(i," ", j)

#wap to move *
# char = str(input("Enter a character: "))
# output_str ="*" * char.count("*") + char.replace("*","")
# print(output_str)


# a = 50
# b = 30
# c = 10
# d = 20
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# x = ['A', 'B', 'C']
# y = ['A', 'B', 'C']
# z = [1,2,3,4]
# print( (x==y))
# print( (x==z))
# print((x != z))


# wap to check if two strings are anagrams of other
# logic : check if the character count in both string are the same
# str1 = "listen"
# str2 = "silent"
# if sorted(str1) == sorted(str2):
#     print("Anagram")
# else:
#     print("Not Anagram")

#count words in a string
#This is the sentences. input
# str = "This is my the sentences."
# c1 = len(str.split()) #split use here because split() breaks a sentnces into individual words.
# print(c1)


# str1 = "This is the sentnces."
# count =1
# for i in str1:
#     if i == ' ' :
#         count+=1
# print(count)


#given an array , return an array where each element is the product of all the elements in the array except itself.
#input: [1,2,3,4]
#expected output:- [24, 12, 8, 6]
# s = [1, 2, 3, 4]







# arr = [[1,2,3,4], 
#        [5,6,7,8],
#        [9,10,11,12],
#        [13,14,15,16]]#it is a 2D list or a list of lists
# for i in range(0, 4):#it will iterate through the outer list and print the inner lists
#     print(arr[i].pop())