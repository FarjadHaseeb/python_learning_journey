import json
from pathlib import Path

file = Path("expenses.json")

if file.exists():
    expenses = json.loads(file.read_text())
else:
    expenses = []

name = input("Expense name: ")
amount = float(input("Amount: "))
expenses.append({"name": name, "amount": amount})

file.write_text(json.dumps(expenses, indent=4))
print("Saved to", file)
