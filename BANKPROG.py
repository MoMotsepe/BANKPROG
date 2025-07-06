import datetime

class User:
    def __init__(self, name, age, income):
        self.name = name
        self.age = age
        self.income = income
        self.balance = 0.0
        self.package = None
        self.transactions = []

    def add_transaction(self, type_, amount):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append((now, type_, amount))
        if type_ == "Deposit":
            self.balance += amount
        elif type_ == "Withdrawal":
            self.balance -= amount

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print(f"Transaction History for {self.name}:")
            for t in self.transactions:
                print(f"{t[0]} - {t[1]}: R{t[2]:.2f}")

def input_nonempty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")

def input_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt).strip())
            if val >= 0:
                return val
            else:
                print("Value must be zero or positive.")
        except ValueError:
            print("Please enter a valid number.")

def input_positive_int(prompt):
    while True:
        val = input(prompt).strip()
        if val.isdigit() and int(val) > 0:
            return int(val)
        else:
            print("Please enter a valid positive integer.")

def select_package():
    print("Available packages:")
    print("1. INCREASER - Double your monthly income as simulated monthly benefit")
    print("2. SAVER - Save 1% of your monthly income every month")
    print("3. INVESTOR - Gain 5% interest monthly on your current balance")
    
    while True:
        choice = input("Select a package (1/2/3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Choose 1, 2, or 3.")

def process_package(user, package_choice):
    if package_choice == "1":
        user.package = "INCREASER"
        benefit = user.income * 2
        print(f"INCREASER Package: You will receive roughly R{benefit:.2f} per month for the rest of the year.")
        user.add_transaction("Deposit", benefit)
    elif package_choice == "2":
        user.package = "SAVER"
        saving = user.income * 0.01
        print(f"SAVER Package: You will save R{saving:.2f} monthly.")
        user.add_transaction("Deposit", saving)
    elif package_choice == "3":
        user.package = "INVESTOR"
        interest = user.balance * 0.05
        print(f"INVESTOR Package: You will gain R{interest:.2f} monthly on your current balance.")
        user.add_transaction("Deposit", interest)

def bank_menu():
    users = []

    while True:
        print("\nWelcome to the Python Bank System!")
        print("1. Register a new user")
        print("2. Show all users")
        print("3. Select user")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            name = input_nonempty_string("Enter your name: ")
            age = input_positive_int("Enter your age: ")
            income = input_positive_float("Enter your monthly income: ")

            if age < 18:
                print("Sorry, you must be at least 18 years old to register.")
                continue
            if income < 200:
                print("Sorry, income must be at least R200 to be eligible.")
                continue

            user = User(name, age, income)
            users.append(user)
            print(f"User {name} registered successfully.")

            # Select package for new user
            package_choice = select_package()
            process_package(user, package_choice)

        elif choice == "2":
            if not users:
                print("No registered users yet.")
            else:
                print("Registered Users:")
                for i, u in enumerate(users, start=1):
                    print(f"{i}. {u.name}, Age: {u.age}, Income: R{u.income:.2f}, Balance: R{u.balance:.2f}, Package: {u.package or 'None'}")

        elif choice == "3":
            if not users:
                print("No users to select.")
                continue

            for i, u in enumerate(users, start=1):
                print(f"{i}. {u.name}")
            idx = input_positive_int("Select user by number: ") - 1
            if idx < 0 or idx >= len(users):
                print("Invalid user number.")
                continue

            user = users[idx]
            print(f"Selected user: {user.name}")

            while True:
                print(f"\nUser Menu - {user.name}")
                print("1. View balance")
                print("2. Deposit money")
                print("3. Withdraw money")
                print("4. View transactions")
                print("5. Change package")
                print("6. Back to main menu")
                sub_choice = input("Choose an option (1-6): ").strip()

                if sub_choice == "1":
                    print(f"Current balance: R{user.balance:.2f}")
                elif sub_choice == "2":
                    amount = input_positive_float("Enter amount to deposit: ")
                    user.add_transaction("Deposit", amount)
                    print(f"Deposited R{amount:.2f}. New balance: R{user.balance:.2f}")
                elif sub_choice == "3":
                    amount = input_positive_float("Enter amount to withdraw: ")
                    if amount > user.balance:
                        print("Insufficient balance.")
                    else:
                        user.add_transaction("Withdrawal", amount)
                        print(f"Withdrew R{amount:.2f}. New balance: R{user.balance:.2f}")
                elif sub_choice == "4":
                    user.show_transactions()
                elif sub_choice == "5":
                    package_choice = select_package()
                    process_package(user, package_choice)
                elif sub_choice == "6":
                    break
                else:
                    print("Invalid choice.")

        elif choice == "4":
            print("Thank you for using the Python Bank System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    bank_menu()
