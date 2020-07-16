import string
import random

def generator(options, length):
    password = ""
    long_chars = "".join(options.values())
    for _ in range(length):
        password += random.choice(long_chars)

    return password

def main():
    print("Password Generator".center(50))
    
    length = int(input("Password length: "))

    options = {
        "numbers": string.digits,
        "lower case": string.ascii_lowercase,
        "upper case": string.ascii_uppercase,
        "special characters": string.punctuation + " "
    }

    print("Complexity")
    print("Enter 0 to exclude, any other value will be accepted")
    for index, option in enumerate(options.keys()):
        selected = input(f"{index + 1}. {option.capitalize()}: ")
        if selected == '0':
            options[option] = ""

    if not any(options.values()) or length <= 0:
        print("Password can not be generated.")
    else:
        password = generator(options, length)
        print(f"Your secure password is {password}")

if __name__ == "__main__":
    main()