# # wap to accept any one character from keyboard and check it is in uppper case, lowercase, digit or  special symbol so print message with respect to entered value

# char = input("Enter a character: ")
# if char.isupper():
#     print("The character is in uppercase.")
# elif char.islower():
#     print("The character is in lowercase.")
# elif char.isdigit():
#     print("The character is a digit.")
# else:
#     print("The character is a special symbol.")


# asccii value of character using ord() function
char = input("Enter a character: ")
ascii_value = ord(char)
print("The ASCII value of the character is: ", ascii_value)
if 65 <= ascii_value <= 90:
    print("The character is in uppercase.")
elif 97 <= ascii_value <= 122:
    print("The character is in lowercase.")
elif 48 <= ascii_value <= 57:
    print("The character is a digit.")
else:
    print("The character is a special symbol.")
    

    
