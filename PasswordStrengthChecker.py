#Password Strength Checker
#ask for input 
password = input("Enter your password to check its strength!: ")
bad = 0
if len(password) < 8:
    print("Your password is too short, it must be at least 8 characters long.")
    bad += 1
if password.islower() | password.isdigit():
    print("Your password must contain at least one uppercase letter.")
    bad += 1
if password.isupper() | password.isdigit(): 
    print("Your password must contain at least one lowercase letter.")
    bad += 1
if password.isalpha():
    print("Your password must contain at least one number or special character.")
    bad += 1
if password.isalnum():
    print("Your password must contain at least one special character.")
    bad += 1
if bad == 0:
    print("Your password is strong! 💪🏽")
else:
    print("Your password is weak, please try again.")
    print("You have", bad, "issues with your password.")