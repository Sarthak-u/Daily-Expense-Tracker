# main.py
from auth import AuthManager
from expenses import ExpenseManager
from reports import ReportManager
import sys

def main():
    print("Welcome to Personal Expense Tracker")

    auth = AuthManager("data/users.csv")
    user = None

    while not user:
        print("\n1) Signup\n2) Login\n3) Exit")
        c = input("Choose: ")

        if c == "1":
            u = input("Username: ")
            p = input("Password: ")
            try:
                auth.signup(u, p)
                print("Signup successful.")
            except Exception as e:
                print("Error:", e)

        elif c == "2":
            u = input("Username: ")
            p = input("Password: ")
            user = auth.login(u, p)
            if not user:
                print("Invalid login.")
        else:
            sys.exit()

    print("Logged in as:", user["username"])
    manager = ExpenseManager(f"data/{user['username']}_expenses.csv")
    reports = ReportManager(manager)

    while True:
        print("\n1) Add Expense\n2) View Expenses\n3) Summary\n4) Export CSV\n5) Exit")
        c = input("Choose: ")

        if c == "1":
            title = input("Title: ")
            amount = float(input("Amount: "))
            category = input("Category: ") or "other"
            date = input("Date (YYYY-MM-DD): ") or None
            tag = input("Tag: ")
            manager.add_expense(title, amount, category, date, tag)

        elif c == "2":
            manager.list_expenses()

        elif c == "3":
            reports.monthly_summary()

        elif c == "4":
            manager.export_csv("export.csv")
            print("Exported to export.csv")

        else:
            sys.exit()

if __name__ == "__main__":
    main()
