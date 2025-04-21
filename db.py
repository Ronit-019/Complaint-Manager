import json
import os

class Database:
    def __init__(self):
        self.users_file = "users.json"
        self.complaints_file = "complaints.json"

        # Initialize the files if they don't exist
        if not os.path.exists(self.users_file):
            with open(self.users_file, "w") as f:
                json.dump([], f)

        if not os.path.exists(self.complaints_file):
            with open(self.complaints_file, "w") as f:
                json.dump([], f)

    # Register a new user
    def insert(self, name, email, password):
        with open(self.users_file, "r+") as f:
            users = json.load(f)

            # Check if email already exists
            for user in users:
                if user['email'] == email:
                    return False

            users.append({
                "name": name,
                "email": email,
                "password": password
            })
            f.seek(0)
            json.dump(users, f, indent=4)
            return True

    # Authenticate user
    def search(self, email, password):
        with open(self.users_file, "r") as f:
            users = json.load(f)

            for user in users:
                if user["email"] == email and user["password"] == password:
                    return True
        return False

    # Insert complaint data
    def insertco(self, email, title, desc, categ, loc, dat, photo_path, urg):
        with open(self.users_file, "r") as f:
            users = json.load(f)

            # Ensure user exists
            user_exists = any(user["email"] == email for user in users)
            if not user_exists:
                return 0

        with open(self.complaints_file, "r+") as f:
            complaints = json.load(f)

            complaints.append({
                "email": email,
                "title": title,
                "description": desc,
                "category": categ,
                "location": loc,
                "date": dat,
                "photo": photo_path,
                "urgency": urg
            })

            f.seek(0)
            json.dump(complaints, f, indent=4)
            return 1
