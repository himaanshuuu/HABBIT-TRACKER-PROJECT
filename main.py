import json
import random
import string
from pathlib import Path
from datetime import date


class HABITRACKER:

    database = Path(__file__).parent / "data.json"

    # ---------------- INIT ----------------
    def __init__(self):
        self.data = self.load_data()

    # ---------------- LOAD DATABASE ----------------
    def load_data(self):
        if self.database.exists():
            try:
                with open(self.database, "r") as file:
                    return json.load(file)
            except:
                return []
        return []

    # ---------------- SAVE DATABASE ----------------
    def save_data(self):
        with open(self.database, "w") as file:
            json.dump(self.data, file, indent=4)

    # ---------------- GENERATE ACCOUNT NUMBER ----------------
    def generate_account_number(self):
        alpha = random.choices(string.ascii_letters, k=2)
        num = random.choices(string.digits, k=2)
        spchar = random.choices("!@#$%^&*()", k=2)
        acc_id = alpha + num + spchar
        random.shuffle(acc_id)
        return "".join(acc_id)

    # ---------------- DESCRIPTION ----------------
    def DESCRIPTION(self):
        print("\nHabit Tracker is a discipline-focused system.")
        print("Every day you either execute or reset.")
        print("No excuses.\n")

    # ---------------- RULES ----------------
    def RULES(self):
        print("\n1. Only completed habits count.")
        print("2. Miss a day, streak resets.")
        print("3. No fake entries.")
        print("4. You cannot log habits twice in one day.\n")

    # ---------------- FEATURES ----------------
    def FEATURES(self):
        print("\nTrack habits")
        print("Daily records")
        print("Streak system")
        print("Automatic reset\n")

    # ---------------- CREATE ACCOUNT ----------------
    def CREATE_ACCOUNT(self):

        name = input("Enter Full Name: ")
        age = int(input("Enter Age: "))
        email = input("Enter Email: ")
        pin = int(input("Set 4-digit PIN: "))

        habits = []
        total = int(input("How many habits do you want to track? "))

        for i in range(total):
            habit = input(f"Enter habit {i+1}: ")
            habits.append(habit)

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "AccountNo": self.generate_account_number(),
            "habits": habits,
            "records": {},
            "streak": 0
        }

        self.data.append(account)
        self.save_data()

        print("\nAccount Created Successfully!")
        print("Your Account Number:", account["AccountNo"])
        print("STAY HARD.")

    # ---------------- LOGIN + DAILY CHECK ----------------
    def LOGIN(self):

        accountnumber = input("Enter Account Number: ")
        pin = int(input("Enter PIN: "))

        for user in self.data:

            if user["AccountNo"] == accountnumber and user["pin"] == pin:

                print(f"\nWelcome back {user['name']}!")

                today = str(date.today())

                if today in user["records"]:
                    print("You have already submitted today's habits.")
                else:
                    user["records"][today] = {}
                    all_completed = True

                    print("\nDAILY HABIT CHECK\n")

                    for habit in user["habits"]:
                        ans = input(f"Did you complete '{habit}' today? (yes/no): ")

                        if ans.lower() == "yes":
                            user["records"][today][habit] = True
                        else:
                            user["records"][today][habit] = False
                            all_completed = False

                    if all_completed:
                        user["streak"] += 1
                    else:
                        user["streak"] = 0

                    self.save_data()

                    print("\nData saved successfully.")
                    print("Current streak:", user["streak"])

                # -------- NEW FEATURE ADDED HERE --------
                view = input("\nDo you want to see your full progress till now? (yes/no): ")

                if view.lower() == "yes":

                    print("\nFULL PROGRESS REPORT\n")

                    if not user["records"]:
                        print("No records found.")
                    else:
                        for record_date, habits_data in user["records"].items():
                            print("Date:", record_date)
                            for habit, status in habits_data.items():
                                result = "Completed" if status else "Not Completed"
                                print(f"  {habit}: {result}")
                            print()

                    print("Current Streak:", user["streak"])

                print("STAY HARD.")
                return

        print("Invalid Account Number or PIN.")
        print("STAY HARD.")


# ---------------- MAIN PROGRAM ----------------

app = HABITRACKER()

while True:

    print("\nWELCOME TO THE PAIN ZONE\n")
    print("1. DESCRIPTION")
    print("2. RULES")
    print("3. FEATURES")
    print("4. CREATE ACCOUNT")
    print("5. LOGIN")
    print("6. EXIT\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        app.DESCRIPTION()

    elif choice == "2":
        app.RULES()

    elif choice == "3":
        app.FEATURES()

    elif choice == "4":
        app.CREATE_ACCOUNT()

    elif choice == "5":
        app.LOGIN()

    elif choice == "6":
        print("STAY HARD.")
        break

    else:
        print("Invalid choice.")
        print("STAY HARD.")