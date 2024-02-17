import datetime
import json

def load_data():
    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"expenses": []}
    return data

def save_data(data):
    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=2)

def add_expense(data, amount, category):
    expense = {
        "date": str(datetime.datetime.now()),
        "amount": amount,
        "category": category
    }
    data["expenses"].append(expense)
    save_data(data)
    print("Expense added successfully.")

def view_expenses(data):
    expenses = data["expenses"]
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Expense History:")
        for expense in expenses:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}")

def view_spending_patterns(data):
    expenses = data["expenses"]
    if not expenses:
        print("No expenses recorded.")
    else:
        category_totals = {}
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]
            category_totals[category] = category_totals.get(category, 0) + amount

        print("Spending Patterns:")
        for category, total in category_totals.items():
            print(f"Category: {category}, Total Amount: {total}")

def main():
    data = load_data()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Patterns")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            add_expense(data, amount, category)
        elif choice == '2':
            view_expenses(data)
        elif choice == '3':
            view_spending_patterns(data)
        elif choice == '4':
            print("Exiting the expense tracking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
