import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def power(a, b):
    result = a ** b
    if isinstance(result, complex):
        raise ValueError("complex")
    return result


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a % b


def show_menu():
    print("\n===== Menu-Driven Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")


def get_number(prompt):
    value = float(input(prompt))
    if not math.isfinite(value):
        raise ValueError("not finite")
    return value


def fmt(n):
    # input numbers ko clean dikhane ke liye (12.0 -> 12, 9.5 -> 9.5)
    return str(int(n)) if n == int(n) else str(n)


def main():
    operations = {
        1: ("+", add),
        2: ("-", subtract),
        3: ("*", multiply),
        4: ("/", divide),
        5: ("^", power),
        6: ("%", modulus),
    }

    while True:
        show_menu()
        choice_text = input("Enter your choice (1-7): ").strip()

        try:
            choice = int(choice_text)
        except ValueError:
            print("Invalid choice. Select 1 to 7.")
            continue

        if choice == 7:
            print("Thank you for using the calculator. Exiting...")
            break

        if choice not in operations:
            print("Invalid choice. Select 1 to 7.")
            continue

        symbol, func = operations[choice]

        try:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
        except ValueError:
            print("Invalid number. Enter numeric values only.")
            continue

        try:
            result = func(num1, num2)
            print(f"{fmt(num1)} {symbol} {fmt(num2)} = {result:.2f}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except OverflowError:
            print("Error: Result is too large.")
        except ValueError:
            print("Error: Result is not a real number.")


if __name__ == "__main__":
    main()