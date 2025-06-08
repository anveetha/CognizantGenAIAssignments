#About Parameters of Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(num1, num2):
    return num1 + num2

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type} named {pet_name.title()}.")

def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n): 
    if n == 1:
        return 0
    else:
        for i in range(1, n + 1):
            if i == 1:
                a, b = 0, 1
            else:
                a, b = b, a + b
        return b

nameIn = input("Enter your name: ")
greet_user(nameIn)

num1 = 5
num2 = 10
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}.")

describe_pet('Buddy')
describe_pet('Whiskers', 'cat')

ingredients = ['lettuce', 'tomato', 'turkey', 'cheese']
make_sandwich(*ingredients)

print(f"The factorial of 5 is {factorial(5)}.")
print(f"The {2}th Fibonacci number is {fibonacci(2)}.")