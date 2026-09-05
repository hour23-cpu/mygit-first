class ExpenseTracker:
    def __init__(self):
        # Initializes an empty list to hold all recorded expenses.
        self.expenses = []

    def add_expense(self, amount, description, category):
        # Appends a new expense record (amount, description, category) to the list.
        self.expenses.append({"amount": amount, "description": description, "category": category})

    def monthly_summary(self):
        # Sums the amount of every recorded expense and returns the total.
        monthly_total = sum(expense["amount"] for expense in self.expenses)
        return monthly_total

    def category_expenditure(self):
        # Groups expenses by category and returns a dict of total amount spent per category.
        category_expenses = {}
        for expense in self.expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in category_expenses:
                category_expenses[category] += amount
            else:
                category_expenses[category] = amount
        return category_expenses

class UserInterface:
    def __init__(self, tracker):
        # Stores a reference to the ExpenseTracker instance this UI operates on.
        self.tracker = tracker

    def input_expense(self):
        # Prompts the user for amount, description, and category, then adds the expense.
        amount = float(input("Enter amount spent: "))
        description = input("Enter brief description: ")
        category = input("Enter expense category: ")
        self.tracker.add_expense(amount, description, category)
        print("Expense added successfully!")

    def display_monthly_summary(self):
        # Fetches and prints the total of all expenses recorded so far.
        total_expenses = self.tracker.monthly_summary()
        print("---------------------------------------")
        print("Monthly Total Expenses:", total_expenses)
        print("---------------------------------------")

    def display_category_expenditure(self):
        # Fetches and prints the total spent in each expense category.
        category_expenses = self.tracker.category_expenditure()
        print("---------------------------------------")
        print("Category-wise Expenditure:")
        for category, amount in category_expenses.items():
            print(f"{category}: {amount}")
        print("---------------------------------------")

    def run(self):
        # Main menu loop: repeatedly shows options and dispatches to the chosen action until exit.
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Monthly Summary")
            print("3. View Category-wise Expenditure")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.input_expense()
            elif choice == '2':
                self.display_monthly_summary()
            elif choice == '3':
                self.display_category_expenditure()
            elif choice == '4':
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    ui = UserInterface(tracker)
    ui.run()
    