# reports.py
from storage import read_rows
from collections import defaultdict

class ReportManager:
    def __init__(self, manager):
        self.manager = manager

    def monthly_summary(self):
        rows = read_rows(self.manager.csv)
        totals = defaultdict(float)
        for r in rows:
            month = r["date"][:7]
            totals[month] += float(r["amount"])
        print("Monthly Summary:")
        for m, v in sorted(totals.items()):
            print(m, v)
