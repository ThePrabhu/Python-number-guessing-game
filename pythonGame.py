import random
import time

print("Hey! Welcome to Random Number Guessing Game.\nLet's Start! ❤️‍🔥")
time.sleep(1)
print("You have seven chances to guess the correct number. Best of Luck!")

def number_guessing_game():
    try:
        Low = int(input("Enter Lower bound to begin: "))
        time.sleep(1)
        High = int(input("Enter Higher bound to begin: "))
    except ValueError:
        print("Error❌ : Enter integers to continue")
        return

    num = random.randint(Low, High)
    chances = 7
    tries = 0

    while tries < chances:
        tries += 1
        try:
            Guess = int(input(f'Enter your guess #{tries}: '))
        except ValueError:
            print("Error❌ : Enter integers to continue")
            continue

        if Guess == num:
            print("🎊 Congratulations! Your guess is correct.")
            break
        elif Guess > num:
            print("Your guess is too high!")
        elif Guess < num:
            print("Your guess is too low!")

        if tries == chances:
            print(f"😢 Sorry! You've used all your chances. The number was {num}. Better luck next time.")

number_guessing_game()