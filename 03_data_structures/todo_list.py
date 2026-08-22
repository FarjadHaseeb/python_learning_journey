tasks = []

while True:
    print("\n1. Add  2. View  3. Remove  4. Quit")
    choice = input("Choice: ")

    if choice == "1":
        tasks.append(input("Task: "))
    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            print(i, task)
    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(i, task)
        try:
            tasks.pop(int(input("Task number: ")) - 1)
        except (ValueError, IndexError):
            print("Invalid task")
    elif choice == "4":
        break
