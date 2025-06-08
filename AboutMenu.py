#About Menu
print("Please select an option: \n1. Calculate the factorial of a number. \n2.Find an nth Fibonacci number. \n3. Draw a recursive fractal pattern. \n4. Exit.")
choice = input("Enter your choice (1-4): ")
if choice == '1':
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    num = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {num} is {factorial(num)}.")
elif choice == '2':
    def fibonacci(n):
        if n == 1:
            return 0
        a, b = 0, 1
        for _ in range(2, n):  # Fixed loop range
            a, b = b, a + b
        return b

    n = int(input("Enter the position of the Fibonacci sequence to retrieve: "))
    print(f"The {n}th Fibonacci number is {fibonacci(n)}.")

elif choice == '3':
    n = int(input("Enter the depth of the fractal pattern: "))
    def draw_fractal(pattern, depth):
        if depth == 0:
            print(pattern)
        else:
            draw_fractal(pattern + "  ", depth - 1)
            draw_fractal(pattern + "* ", depth - 1)
    def draw_symmetrical_fractal(pattern, depth, indent=0): # fractal pattern, no usage of turtle library
        if depth == 0:
            print(' ' * indent + pattern)
        else:
            draw_symmetrical_fractal(pattern + "*", depth - 1, indent + 1)
            draw_symmetrical_fractal(pattern + " ", depth - 1, indent + 1)

    draw_symmetrical_fractal("", n)
elif choice == '4':
    print("Exiting the program. Goodbye!")
else:
    print("Invalid choice. Please select a valid option (1-4).")

    