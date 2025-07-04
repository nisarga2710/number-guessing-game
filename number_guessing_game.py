import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
secret_number = random.randint(1,100)
attempts = 0
max_attempts = 7
while attempts<max_attempts:
    try:
        guess=int(input(f"\nAttempt{attempts+1}of{max_attempts}-Enter your guess:"))
        attempts+=1
        if guess<secret_number:
            print("Too low!")
        elif guess>secret_number:
            print("too high!")
        else:
            print(f"correct!you guessed the number in {attempts}attempts!")
            break
    except ValueError:
        print("Please enter a valid number!")
if attempts == max_attempts and guess !=secret_number:
    print(f"\n you have run out of attempts.The number was {secret_number}.Better luck next time!")