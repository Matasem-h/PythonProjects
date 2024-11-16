import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")

numbers = range(101)
goal_number = random.choice(numbers)
print("I'm thinking of a number between 1 and 100.")

difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty_choice == 'easy':
    attempts = 10  # This is to set the initial number of attempts
    for i in range(attempts):
        guess = int(input(f"Try to guess the correct number! You have {attempts} remaining. \n"))
        if guess == goal_number:
            print(f"You guessed the correct number! It was {goal_number}")
        if guess > goal_number:
            print("Too high!")
        elif guess < goal_number:
            print("Too low!")

        attempts -= 1
        if attempts == 0:
            print("You have no more attempts! You have lost.")
            print(f"The correct number was {goal_number}")


elif difficulty_choice == 'hard':
    attempts = 5
    for i in range(attempts):
        guess = int(input(f"Try to guess the correct number! You have {attempts} left. \n"))
        if guess == goal_number:
            print(f"You guessed the correct number! It was {goal_number}")
        if guess > goal_number:
            print("Too high!")
        elif guess < goal_number:
            print("Too low!")

        attempts -= 1
        if attempts == 0:
            print("You have no more attempts! You have lost.")
            print(f"The correct number was {goal_number}")
