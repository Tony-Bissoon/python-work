# # write a for loop that iterates through this dictionary and prints the key followed by the value using f shorthand
# csx = {
#     "mp1": "hardware",
#     "mp2": "skinny py",
#     "mp3": "python basics",
#     "mp4": "advanced OOP"
# }

# for i in csx: 
#     print(f"{i} {csx[i]}")

# # write a while loop that prints out while_num, decrements it by 1, and continues this pattern until it reaches zero
# while_num = 10
# while while_num:
#     print(while_num)
#     while_num = while_num - 1

revenue = int(input("How much did your product earn in Revenue?: "))

expenses = 0 
is_yes = True
while is_yes:
    response = input("Does your business have any expenses to add? Y/N): ")
    if (response == "Y"):
        new_expense = int(input("Enter Expense: " ))
        expenses = expenses + new_expense
    else: 
        is_yes = False

profit = revenue - expenses
print(f"Your product had ${revenue:.2f} in revenue, ${expenses:.2f} in total expenses, and a profit of ${profit:.2f}")




