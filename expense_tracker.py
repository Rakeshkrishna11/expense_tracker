import os

FILENAME = "expenses.txt"

def add_expense():
    item = input("Enter item name: ")
    amount = input("Enter amount: ₹")
    with open(FILENAME, "a") as file:
        file.write(f"{item},{amount}\n")
    print("✅ Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found.\n")
        return
    print("\n📋 All Expenses:")
    with open(FILENAME, "r") as file:
        for line in file:
            item, amount = line.strip().split(",")
            print(f"- {item}: ₹{amount}")
    print()

def total_expenses():
    total = 0
    if not os.path.exists(FILENAME):
        print("No expenses to calculate.\n")
        return
    with open(FILENAME, "r") as file:
        for line in file:
            _, amount = line.strip().split(",")
            total += float(amount)
    print(f"\n💰 Total Expenses: ₹{total}\n")

def delete_expense():
    view_expenses()
    name = input("Enter the name of the item to delete: ")
    if not os.path.exists(FILENAME):
        print("No expenses found.\n")
        return
    lines = []
    with open(FILENAME, "r") as file:
        lines = file.readlines()
    with open(FILENAME, "w") as file:
        found = False
        for line in lines:
            if line.startswith(name + ","):
                found = True
                continue
            file.write(line)
    if found:
        print("🗑️ Expense deleted.\n")
    else:
        print("❌ Expense not found.\n")

def main():
    while True:
        print("📊 Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
