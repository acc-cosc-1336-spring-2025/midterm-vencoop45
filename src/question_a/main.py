#add import
from question_a import get_person_category
def main():
    while True:
        try:
            age_str = input("Please enter individual's age - or type 'quit' to exit:")
            if age_str.lower() == 'quit':
                break
            age = int(age_str)
            category = get_person_category(age)
            print(f"The individual is a(n) {category}.")
        except ValueError as e:
            print("Invalid input. Please enter a whole number for the age or 'quit'.")

if __name__ == '__main__':
   main() 