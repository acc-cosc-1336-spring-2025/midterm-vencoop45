#add import
from question_c import get_fahrenheit

def main():
    print("Celsius\tFahrenheit")
    print("-------\t-------")
    for celsius in range(21):
        fahrenheit = get_fahrenheit(celsius)
        print(f"{celsius}\t\t{fahrenheit:.1f}")
    
if __name__ == "__main__":
    main()

