#Task 1 
name = "Anveetha" 
age = 20
height = 5.3
print("Hello, my name is", name, ". I am", age, "years old, and my height is", height, "feet.") 

#Task 2
num1 = 10 
num2 = 5
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)
difference = num1 - num2
print("The difference between", num1, "and", num2, "is", difference)
product = num1 * num2
print("The product of", num1, "and", num2, "is", product)
quotient = num1 / num2
print("The quotient of", num1, "and", num2, "is", quotient)

#Task 3
num = input("Enter a number: ")
num = int(num)  # Convert input to integer
if (num > 0):
    print("The number is positive.")
elif (num < 0):
    print("The number is negative, better luck next time!")
else:
    print("The number is zero, perfect balance!")