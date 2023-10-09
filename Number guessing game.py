# NUMBER GUESSING GAME

import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
"""
random_num = random.choice(range(10, 101))

def easy():
    attempts = 10
    not_correct = True

    while not_correct:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > random_num:
            attempts -= 1
            print("Too high.")

        elif guess < random_num:
            attempts -= 1
            print("Too low.")

        elif guess == random_num:
            not_correct = False
            print(f"You got it! The answer was {random_num}.")

        if attempts ==  0:
            print("You've run out of guesses, you lose.")


def hard():
    attempts = 5
    not_correct = True

    while not_correct:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > random_num:
            attempts -= 1
            print("Too high.")

        elif guess < random_num:
            attempts -= 1
            print("Too low.")

        elif guess == random_num:
            not_correct = False
            print(f"You got it! The answer was {random_num}.")

        if attempts == 0 :
            not_correct = False
            print("You've run out of guesses, you lose.")

print(logo)
print("Welcome to the Number Guessing Game! ")
print("I am thinking of a number between 1 and 100.")
# print(f"pssst the correct answer is {random_num}")

while True:
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if choice == "easy":
        easy()
        break

    elif choice == "hard":
        hard()
        break

    else:
        print("Try again.")
