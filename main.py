# Expense Tracker Project
expenses = []  # List to store all expenses

print("Welcome To Expense Tracker")

while True:
    print("\n=== MENU ===")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Show Highest Expense")
    print("5. Exit")
    
    choise = int(input("Enter Your Choice: "))
    
    # 1. Add Expense
    if choise == 1:
        date = input("Enter the date: ")
        category = input("Enter category (ex. products, food, books): ")
        description = input("Enter description: ")
        amount = float(input("Enter the amount: "))
        
        expense = {
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount
        }
        expenses.append(expense)
        print("\nExpense added successfully!")
        
    # 2. View All Expenses
    elif choise == 2:
        if len(expenses) == 0:
            print("No expense added yet.")
        else:
            print("\n==== All Expenses ====")
            count = 1
            for ex in expenses:
                print(f"{count}. {ex['Date']} | {ex['Category']} | {ex['Description']} | ₹{ex['Amount']}")
                count += 1
                
    # 3. View Total Expense
    elif choise == 3:
        total = 0
        for ex in expenses:
            total += ex["Amount"]
        print("\nTotal Expense:", total)
        
    # 4. Show Highest Expense
    elif choise == 4:
        if len(expenses) == 0:
            print("No expense added yet.")
        else:
            max_amount = 0
            for ex in expenses:
                if ex["Amount"] > max_amount:
                    max_amount = ex["Amount"]
            print("\nHighest Expense is:", max_amount)
            
    # 5. Exit
    elif choise == 5:
        print("Thanks for using our system!")
        break
        
    else:
        print("Invalid Choice! Try again.")
