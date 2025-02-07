import random
from art import logo

print(logo)
chose_no=random.randint(1,100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
easy_or_hard=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
hard_lives=5
easy_lives=10
game_over=True
while game_over:
    if easy_or_hard =="easy":
        print(f"You have {easy_lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == chose_no:
            print(f"You got it! The answer was {chose_no} .")
            game_over=False
        if guess != chose_no:
            easy_lives -=1
            if guess > chose_no:
                print("Too high")
            elif guess < chose_no:
                print("Too low")
            else:
                print("Invalid input")

            if easy_lives==0:
                print("You've run out of guesses. Refresh the page to run again.")
                game_over=False
            elif guess != chose_no:
                print("Guess again")

    if easy_or_hard =="hard":
        print(f"You have {hard_lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == chose_no:
            print(f"You got it! The answer was {chose_no} .")
            game_over=False
        if guess != chose_no:
            hard_lives -=1
            if guess > chose_no:
                print("Too high")
            elif guess < chose_no:
                print("Too low")
            else:
                print("Invalid input")

            if hard_lives==0:
                print("You've run out of guesses. Refresh the page to run again.")
                game_over=False
            elif guess != chose_no:
                print("Guess again")