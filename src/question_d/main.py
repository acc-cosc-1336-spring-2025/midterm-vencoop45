#add import
from question_d import get_sum_of_evens

def main():
    while True:
        try:
            user_input = input("Enter a number - or 'quit' to exit:")
            if user_input.lower() == 'quit':
                print("Exiting program.")
                break
            number = int(user_input)
            even_sum = get_sum_of_evens(number)
            print(f"The sum of even numbers up to {number} is: {even_sum}")
        except ValueError:
            print("Invalid input. Please enter a whole number or 'quit'.")

if __name__ == "__main__":
    main()