age = int(input("How old are you? "))
if age < 18:
    print("Oops! You are not eligible to vote. But hey, only", 18-age, "more years to go!")
else:
    print("Great! You are eligible to vote. Make your voice heard!")
    