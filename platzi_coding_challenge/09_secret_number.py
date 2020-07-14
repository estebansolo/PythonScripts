import random

def secret_number():
    return random.randint(1, 100)

def main():
    print("Guess the secret number".center(50), "\n")
    print("It's a number from 1 to 100")

    tries = 0
    user_number = 0
    number = secret_number()
    while user_number != number:
        tries += 1
        try:
            user_number = int(input("Insert a numer: "))
        except ValueError:
            print("Invalid number.")
        else:
            if user_number > number:
                print(f"Secret number is less than {user_number}")
            elif user_number < number:
                print(f"Secret number is greater than {user_number}")
    
    print("Congratulations, You guessed the number.")
    print(f"You needed {tries} tries")

if __name__ == "__main__":
    main()