# =========================
# INPUT HELPER FUNCTIONS
# =========================

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Enter a valid integer.")


def get_positive_int(prompt):
    while True:
        num = get_int(prompt)
        if num > 0:
            return num
        print("Enter a positive integer.")


def get_name(prompt):
    while True:
        name = input(prompt).strip()
        if name.isalpha():
            return name
        print("Invalid name! Use only letters.")


def get_non_empty_string(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input cannot be empty.")


def get_int_list(prompt):
    while True:
        try:
            return list(map(int, input(prompt).split()))
        except ValueError:
            print("Invalid list! Enter integers separated by spaces.")


def get_three_marks():
    while True:
        marks = get_int_list("Enter marks of 3 subjects (0-100): ")

        if len(marks) != 3:
            print("Enter exactly 3 marks.")
            continue

        if all(0 <= mark <= 100 for mark in marks):
            return marks

        print("Marks must be between 0 and 100.")


# =========================
# OUTPUT HELPERS
# =========================

def print_table(data):
    for row in data:
        print("     ".join(map(str, row)))


# =========================
# PROBLEM 1: ATM MACHINE
# =========================

def atm_machine():
    balance = 1000
    history = []

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View History")
        print("5. Exit")

        choice = get_int("Choose option: ")

        if choice == 1:
            print(f"Current balance: {balance}")

        elif choice == 2:
            amount = get_positive_int("Deposit amount: ")
            balance += amount
            history.append(("Deposit", amount, balance))
            print("Deposit successful.")

        elif choice == 3:
            amount = get_positive_int("Withdraw amount: ")

            if amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                history.append(("Withdraw", amount, balance))
                print("Withdrawal successful.")

        elif choice == 4:
            if history:
                print("\nType        Amount      Balance")
                print_table(history)
            else:
                print("No transaction history.")

        elif choice == 5:
            break

        else:
            print("Invalid option.")


# =========================
# PROBLEM 2: STUDENT GRADING
# =========================

def student_grading_system():
    students = []

    while True:
        print("\n1. Add Student")
        print("2. Show Students")
        print("3. Exit")

        choice = get_int("Choose option: ")

        if choice == 1:
            name = get_name("Enter student name: ")
            marks = get_three_marks()

            total = sum(marks)
            average = total / len(marks)

            if average >= 90:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 50:
                grade = "C"
            else:
                grade = "Fail"

            students.append((name, total, round(average, 2), grade))

        elif choice == 2:
            if students:
                print("\nName    Total    Average    Grade")
                print_table(students)
            else:
                print("No student records found.")

        elif choice == 3:
            break

        else:
            print("Invalid option.")


# =========================
# PROBLEM 3: FREQUENCY ANALYZER
# =========================

def frequency_analyzer():
    numbers = get_int_list("Enter numbers separated by spaces: ")
    frequency = {}

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    print("\nFrequency:")
    for key, value in frequency.items():
        print(f"{key} → {value}")


# =========================
# PROBLEM 4: PALINDROME CHECKER
# =========================

def palindrome_checker():
    text = get_non_empty_string("Enter text: ")
    cleaned = text.lower().replace(" ", "")

    if cleaned == cleaned[::-1]:
        print("Palindrome.")
    else:
        print("Not palindrome.")


# =========================
# PROBLEM 5: LOGIN SYSTEM
# =========================

def login_system():
    users = {
        "user1": "1234567",
        "user2": "12345678"
    }

    username = get_non_empty_string("Username: ")

    if username not in users:
        print("User not found.")
        return

    attempts = 3

    while attempts > 0:
        password = get_non_empty_string("Password: ")

        if password == users[username]:
            print("Login successful.")
            return

        attempts -= 1
        print(f"Wrong password. {attempts} attempts left.")

    print("Account locked.")


# =========================
# PROBLEM 6: SHOPPING CART
# =========================

def shopping_cart():
    cart = {}

    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Exit")

        choice = get_int("Choose option: ")

        if choice == 1:
            item = get_name("Item name: ").lower()
            cart[item] = cart.get(item, 0) + 1
            print("Item added.")

        elif choice == 2:
            item = get_name("Item name: ").lower()

            if item in cart:
                cart[item] -= 1

                if cart[item] == 0:
                    del cart[item]

                print("Item removed.")
            else:
                print("Item not found.")

        elif choice == 3:
            if cart:
                print("\nItem    Quantity")
                for item, qty in cart.items():
                    print(f"{item}    {qty}")
            else:
                print("Cart is empty.")

        elif choice == 4:
            break

        else:
            print("Invalid option.")


# =========================
# PROBLEM 7: PATTERN
# =========================

def pattern_recognition():
    n = get_positive_int("Enter positive number: ")
    current = 1

    for row in range(1, n + 1):
        for _ in range(row):
            print(current, end=" ")
            current += 1
        print()


# =========================
# MAIN MENU
# =========================

def main():
    while True:
        print("\n========== DAY 02 ==========")
        print("1. ATM Machine")
        print("2. Student Grading System")
        print("3. Frequency Analyzer")
        print("4. Palindrome Checker")
        print("5. Login System")
        print("6. Shopping Cart")
        print("7. Pattern Recognition")
        print("8. Exit")

        choice = get_int("Choose option: ")

        if choice == 1:
            atm_machine()
        elif choice == 2:
            student_grading_system()
        elif choice == 3:
            frequency_analyzer()
        elif choice == 4:
            palindrome_checker()
        elif choice == 5:
            login_system()
        elif choice == 6:
            shopping_cart()
        elif choice == 7:
            pattern_recognition()
        elif choice == 8:
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()