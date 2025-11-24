# auth.py
import csv, os, hashlib

class AuthManager:
    def __init__(self, csv_path):
        self.csv = csv_path
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        if not os.path.exists(csv_path):
            with open(csv_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["username","password_hash"])
                writer.writeheader()

    def _hash(self, pw):
        return hashlib.sha256(pw.encode()).hexdigest()

    def signup(self, username, password):
        if self.exists(username):
            raise Exception("User already exists")
        with open(self.csv, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["username","password_hash"])
            writer.writerow({"username": username, "password_hash": self._hash(password)})

    def exists(self, username):
        with open(self.csv, newline="") as f:
            return any(r["username"] == username for r in csv.DictReader(f))

    def login(self, username, password):
        h = self._hash(password)
        with open(self.csv, newline="") as f:
            for r in csv.DictReader(f):
                if r["username"] == username and r["password_hash"] == h:
                    return {"username": username}
        return None
