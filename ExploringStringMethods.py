#Exploring String Methods
#Task 1 
string = "Python is amazing!"
first6 = string[:6]
amazing = string[10:17]
reverse = string[::-1]
print("First 6 characters:", first6)
print("Substring 'amazing':", amazing)
print("Reversed string:", reverse)

#Task 2 
string2 = " hello, python world! "
stripped = string2.strip()
capitalize = string2.capitalize()
replace = string2.replace("world", "universe")
upper = string2.upper()
print("Stripped string:", stripped)
print("Capitalized string:", capitalize)    
print("Replaced 'world' with 'universe':", replace)
print("Uppercase string:", upper)

#Task 3 
userInput = input("Enter a string!: ")
reversed = userInput[::-1]
if reversed == userInput:
    print("Your word is a palindrome!")
else: 
    print("Your word is not a palindrome, try again!")