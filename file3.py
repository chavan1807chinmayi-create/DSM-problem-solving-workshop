# # for(initialization; condition; increment/decrement)

# for i in range(5):
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)

# for i in range(1,11):
#     print(i*2)

# tables of 2 to 10 and next line is 11 to 20 tables
# for i in range(1, 11):
#     print(i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10)

# print()  # Print a blank line

# for i in range(1, 11):
#     print(i*11, i*12, i*13, i*14, i*15, i*16, i*17, i*18, i*19, i*20)




# with string name
# name = "racear"
#        #012345
# for i in name:
#     print(i)


#wap to remove duplicate characters from string using for loop
# s = "chinmayichavan"
# result = ""
# for i in s:
#     if i not in result:
#         result = result + i
# print(s)
# print(result)

    #wap reverse a string using for loop
# for i in range(5, 0, -1):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

#wap to reverse a string using for loop
# name = "Mumbai"
# for i in range(len(name)-1, -1, -1):
#     print(name[i])


# name = "Mumbai"
# n = len(name)
# for i in range(n-1, -1, -1):
#     print(name[i])


# name = "Mumbai"
# newname = ""
# for i in name:
#     newname = i + newname
# print(newname)


#wap to check if a given string is a palindrome
# name = "Chinamyi"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

char = str(input("Enter a character: "))
print(char)
print(char[::-1])
if char == char[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
