#Task 1 
res = "abc"
while isinstance(res, str):
    try:
        denom = int(input("Please enter a number to divide 100 by:"))
        res = 100 / denom
    except ZeroDivisionError:
        res = "Please do not divide by zero."
    except ValueError:
        res = "Invalid input, please enter a number."
    print(res)

print("Thank you for using the 100/n calculator! Your result:", res)

#Task 2
list = [1, 2, 3, 4, 5]
try: 
    print(list[5])
except IndexError:
    print("Index out of range. Please check the list index.")
dict = {"key1": "value1", "key2": "value2"}
try: 
    print(dict["key3"])
except KeyError:
    print("Key not found. Please check the dictionary keys.")
string = "Hello"
int = 5
try: 
    val = string + int 
except TypeError:
    print("Type mismatch. Unsupported operand types")

#Task 3 
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(f"The result is {result}.")
finally:
    print("Thank you for using the division calculator.")


