# # wap for change calculation with respect to total amount and given amount

# amount = int(input("Enter the amount for withdraw: "))
# print("100 notes = ", amount // 100)
# print("50 notes = ", (amount % 100) // 50)
# print("20 notes = ", ((amount % 100) % 50) // 20)
# print("10 notes = ", (((amount % 100) % 50) % 20) // 10)
# print("5 notes = ", ((((amount % 100) % 50) % 20) % 10) // 5)



# example 2
# amount = int(input("Enter the amount for withdraw: "))
# notes = [100, 50, 20, 10, 5]
# for note in notes:
#     print(f"{note} notes = ", amount // note)
#     amount = amount % note



# example 3
# amount = int(input("Enter the amount for withdraw: "))
# notes = [100, 50, 20, 10, 5]
# for note in notes:
#     count = amount // note
#     print(f"{note} notes = {count}")
#     amount = amount % note

# example 4
# amount = int(input("Enter the amount for withdraw: "))
# notes = [100, 50, 20, 10, 5]
# compare = amount
# for note in notes:
#     count = compare // note
#     print(f"{note} notes = {count}")
#     compare = compare % note
    