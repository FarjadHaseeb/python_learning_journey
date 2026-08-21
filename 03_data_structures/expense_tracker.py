expenses = []

while True:
    print("\n1. Add expense  2. Show total  3. Show expenses  4. Quit")
    choice = input("Choice: ")

    if choice == "1":
        name = input("Expense: ")
        amount = float(input("Amount: "))
        expenses.append({"name": name, "amount": amount})
    elif choice == "2":
        print("Total:", sum(e["amount"] for e in expenses))
    elif choice == "3":
        for expense in expenses:
            print(expense["name"], expense["amount"])
    elif choice == "4":
        break
