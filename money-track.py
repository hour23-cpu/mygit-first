class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category):
        self.expenses.append({
            "amount": amount,
            "description": description,
            "category": category,
        })

    def total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)

    def expenses_by_category(self):
        category_expenses = {}
        for expense in self.expenses:
            category = expense["category"]
            category_expenses[category] = category_expenses.get(category, 0) + expense["amount"]
        return category_expenses


class UserInterface:
    def __init__(self, tracker):
        self.tracker = tracker

    def input_expense(self):
        while True:
            try:
                amount = float(input("Amount spent: $"))
                if amount <= 0:
                    print("Please enter an amount greater than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a number, such as 12.50.")

        description = self.get_text("What was it for? ")
        category = self.get_text("Category (food, travel, bills...): ")
        self.tracker.add_expense(amount, description, category)
        print("Expense saved.")

    @staticmethod
    def get_text(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("This cannot be empty.")

    def display_expenses(self):
        if not self.tracker.expenses:
            print("No expenses recorded yet.")
            return

        print("\nYour expenses:")
        for expense in self.tracker.expenses:
            print(f"- ${expense['amount']:.2f} | {expense['description']} ({expense['category']})")

    def display_total(self):
        print(f"Total spent: ${self.tracker.total_expenses():.2f}")

    def display_category_totals(self):
        category_expenses = self.tracker.expenses_by_category()
        if not category_expenses:
            print("No expenses recorded yet.")
            return

        print("\nSpending by category:")
        for category, amount in category_expenses.items():
            print(f"- {category}: ${amount:.2f}")

    def run(self):
        while True:
            print("\nMoney Tracker")
            print("1. Add an expense")
            print("2. See all expenses")
            print("3. See total spent")
            print("4. See spending by category")
            print("5. Exit")

            choice = input("Choose 1-5: ").strip()
            if choice == "1":
                self.input_expense()
            elif choice == "2":
                self.display_expenses()
            elif choice == "3":
                self.display_total()
            elif choice == "4":
                self.display_category_totals()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    UserInterface(tracker).run()
