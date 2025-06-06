#Task 1 
countdown  = int(input("Enter a number: "))
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")

#Task 2
multiply = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{multiply} x {i} = {multiply * i}")

#Task 3
factorial = int(input("Enter a number: "))
total = 1
for i in range (factorial):
    total *= (i + 1)
print(f"The factorial of {factorial} is {total}")