working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
non_working_days = ["Sunday"]
day = input("Enter the day of the week: ")
if day in working_days:
    print(day, "is a working day.")
elif day in non_working_days:
    print(day, "is a non-working day.")
else:
    print("Weekend!")
    
