#add import
from question_b import get_random_number

def main():
    while True:
        secret_number = get_random_number()
        guesses = 0
        print("\nI'm thinking of a number 1-5, try to guess it!")

        while True:
            try:
                guess_str = input("Please enter your guess - or 'quit' to exit game:")
                if guess_str.lower() == 'quit':
                    break

                guess = int(guess_str)
                guesses += 1

                if guess == secret_number:
                    print(f"Congratulations! You guessed the number {secret_number} in {guesses} tries.")
                    break
                else:
                    print("That isn't what I was thinking of. Try again!")
            except ValueError as e:
                print("Invalid input, enter whole number or 'quit'.")
                
        if guess_str.lower() == 'quit':
            print("Thanks for playing!")
            break