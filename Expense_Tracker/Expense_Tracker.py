import pandas as pd

def initialize_expenses():
    try:
        return pd.read_csv('expenses.csv')
    except FileNotFoundError:
        print("File 'expenses.csv' not found.")

def save_expenses(expenses):
    expenses.to_csv('expenses.csv', index=False)

def add_expense(expenses, date, amount, description, category):
    expenses.loc[len(expenses)] = [date, amount, description, category]
    return expenses

def monthly_summary(expenses):
    expenses['Date'] = pd.to_datetime(expenses['Date'])
    expenses['Month'] = expenses['Date'].dt.strftime('%Y-%m')
    monthly_expenses = expenses.groupby('Month')['Amount'].sum()
    return monthly_expenses

def category_expenditure(expenses):
    category_expenses = expenses.groupby('Category')['Amount'].sum()
    return category_expenses

def main():
    print("Expense Tracker")
    expenses = initialize_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenditure")
        print("4. view Expense History")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount spent: "))
            description = input("Enter description: ")
            category = input("Enter category: ")
            expenses = add_expense(expenses, date, amount, description, category)
            save_expenses(expenses)
            print("Expense added successfully.")

        elif choice == '2':
            monthly_expenses = monthly_summary(expenses)
            print("\nMonthly Expense Summary:")
            print(monthly_expenses)

        elif choice == '3':
            category_expenses = category_expenditure(expenses)
            print("\nCategory-wise Expenditure:")
            print(category_expenses)

        elif choice == '4':
            print("Expenses History")
            print(expenses)

        elif choice == '5':
            print("Exiting Expense Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
