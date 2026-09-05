"""Small terminal number guessing game."""
from random import randint


def play() -> None:
    secret = randint(1, 100)
    attempts = 0
    print("Guess a number from 1 to 100. Type q to quit.")
    while True:
        raw = input("Your guess: ").strip().lower()
        if raw == "q":
            print(f"The number was {secret}.")
            return
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if not 1 <= guess <= 100:
            print("Keep your guess between 1 and 100.")
            continue
        attempts += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! Attempts: {attempts}")
            return


if __name__ == "__main__":
    play()
