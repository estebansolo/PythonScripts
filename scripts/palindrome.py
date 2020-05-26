import re
from string import punctuation

def create_pattern():
    chars = punctuation
    
    chars = list(map(lambda x: re.escape(x), chars))
    chars.append("\s")

    return "|".join(chars)


def palindrome(phrase):
    pattern = create_pattern()
    phrase = re.sub(pattern, "", phrase)

    # Set phrase in lowercase
    phrase = phrase.lower()

    # Conditional Validate
    is_palindrome = phrase == phrase[::-1]

    message = {
        True: f"{phrase} is Palindrome",
        False: f"{phrase} isn't Palindrome"
    }.get(is_palindrome)

    print(message)

if __name__ == "__main__":
    divisor = "*" * 50

    menu = (
        divisor,
        "Palindrome Checker".center(50),
        divisor,
        "Add a phrase, word or number, it will remove",
        "special chars and spaces.",
        divisor
    )
    
    print(*menu, sep="\n")

    data = input("Validate: ")
    palindrome(data)