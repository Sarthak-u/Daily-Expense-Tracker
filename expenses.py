# expenses.py
from storage import read_rows, write_rows, next_id
from datetime import datetime

class ExpenseManager:
    def __init__(self, csv_path):
        self.csv = csv_path

    def add_expense(self, title, amount, category, date, tag):
        rows = read_rows(self.csv)
        if not date:
            date = datetime.today().strftime("%Y-%m-%d")
        rows.append({
            "id": next_id(rows),
            "title": title,
            "amount": f"{amount:.2f}",
            "category": category,
            "date": date,
            "tag": tag
        })
        write_rows(self.csv, rows)

    def list_expenses(self):
        rows = read_rows(self.csv)
        for r in rows:
            print(r)

    def export_csv(self, out):
        rows = read_rows(self.csv)
        with open(out, "w") as f:
            for r in rows:
                f.write(",".join(r.values()) + "\n")
