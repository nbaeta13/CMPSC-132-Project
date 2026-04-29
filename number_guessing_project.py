import random


def play_game():
    secret_number = random.randint(1,100)
    attempts = 0

    print("Welcome to the Number Guessing Game.\n")
    print("I've picked a number between 1 and 100.\n")
    print("Can you guess it?\n")
    
    while True:
        # get user input
        raw = input("Enter your guess: ").strip()

        if not raw.lstrip("-").isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(raw)
        attempts += 1
        
        # feedback
        if guess < secret_number:
            print("Too low- the number is higher than your guess.\n")
        elif guess > secret_number:
            print("Too high- the number is lower than your guess.\n")
        else:
            print("Correct! Congratulations, you guessed the number!\n")
            print(f"The number was {secret_number}.\n")
            print(f"Total attempts: {attempts}\n")
            break




def main():
    while True:
        play_game()
        again = input("\nPlay again?").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing.")
            break
        print()


if __name__ == "__main__":
    main()