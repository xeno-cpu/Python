import random

def guess_the_number():
    target_number = random.randint(1,50)
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 50. Can you guess it?")

    while True:
        # Get user input
        guess = input("> ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < target_number:
            print("Higher!")
        elif guess > target_number:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def main():
    guess_the_number()

if __name__ == "__main__":
    main()

