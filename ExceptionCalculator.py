import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s:%(message)s')

print("Welcome to the Error-Free Calculator!")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("> ")

    if choice == '5':
        print("Goodbye!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid selection! Please choose a valid operation.")
        continue

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logging.error("ValueError occurred: invalid number input for first number.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logging.error("ValueError occurred: invalid number input for second number.")

    try:
        if choice == '1':
            result = num1 + num2
            print(f"The result is: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result is: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result is: {result}")
        elif choice == '4':
            try:
                result = num1 / num2
                print(f"The result is: {result}")
            except ZeroDivisionError as e:
                print("Oops! Division by zero is not allowed.")
                logging.error(f"ZeroDivisionError occurred: {e}")
    except Exception as e:
        print("An unexpected error occurred.")
        logging.error(f"Unexpected error: {e}")
    finally:
        print("This operation has completed.")
