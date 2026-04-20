# ================= UTILITIES =================

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid input. Enter a number.")


# ================= PROBLEM 1: PRIMES =================

def prime_range():
    n = get_int("Enter number: ")
    primes = []

    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    print("Primes:", primes)
    print("Total primes:", len(primes))


# ================= PROBLEM 2: ARMSTRONG =================

def armstrong():
    num = get_int("Enter number: ")
    temp = num
    digits = len(str(num))
    result = 0

    while temp > 0:
        digit = temp % 10
        result += digit ** digits
        temp //= 10

    if num == result:
        print("Armstrong number")
    else:
        print("Not Armstrong")


# ================= PROBLEM 3: PATTERN =================

def pattern():
    n = get_int("Enter n: ")

    for i in range(1, n + 1):
        print(" " * (n - i), end="")

        for j in range(1, i + 1):
            print(j, end="")

        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()


# ================= PROBLEM 4: CALCULATOR =================

def calculator():
    result = get_int("Enter first number: ")

    while True:
        print("\n1:Add 2:Sub 3:Mul 4:Div 5:Exit")
        choice = get_int("Choose: ")

        if choice == 5:
            print("Final result:", result)
            break

        num = get_int("Enter next number: ")

        if choice == 1:
            result += num
        elif choice == 2:
            result -= num
        elif choice == 3:
            result *= num
        elif choice == 4:
            if num != 0:
                result /= num
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid choice")


# ================= PROBLEM 5: PASSWORD =================

def password_checker():
    password = input("Enter password: ")

    if " " in password:
        print("No spaces allowed")
        return

    rules = {
        "length": len(password) >= 8,
        "digit": any(c.isdigit() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "special": any(not c.isalnum() for c in password),
    }

    score = sum(rules.values())

    if score == 4:
        print("Strong")
    elif score >= 2:
        print("Medium")
    else:
        print("Weak")

    print(rules)


# ================= PROBLEM 6: DECIMAL TO BINARY =================

def decimal_to_binary():
    num = get_int("Enter decimal: ")
    binary = ""

    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    print("Binary:", binary)


# ================= PROBLEM 7: SECOND LARGEST =================

def second_largest():
    arr = list(map(int, input("Enter numbers: ").split()))

    largest = second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    print("Second largest:", second)


# ================= MAIN MENU =================

def main():
    while True:
        print("\nChoose Problem:")
        print("1. Prime Range")
        print("2. Armstrong")
        print("3. Pattern")
        print("4. Calculator")
        print("5. Password Checker")
        print("6. Decimal to Binary")
        print("7. Second Largest")
        print("0. Exit")

        choice = get_int("Enter choice: ")

        if choice == 1:
            prime_range()
        elif choice == 2:
            armstrong()
        elif choice == 3:
            pattern()
        elif choice == 4:
            calculator()
        elif choice == 5:
            password_checker()
        elif choice == 6:
            decimal_to_binary()
        elif choice == 7:
            second_largest()
        elif choice == 0:
            break
        else:
            print("Invalid choice")


# ================= ENTRY =================

if __name__ == "__main__":
    main()
        