import random
number_to_guess = random.randint(1, 100)
numGuesses = 0
while(True):
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        numGuesses += 1
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {numGuesses} attempts!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")