import re
import string

digits = string.digits
letters = re.sub(r"[a|e|i|o|u]", "", string.ascii_lowercase)

def word_converter(word):
    if word[0] in digits:
        return word

    if word[0] in letters:
        return f"{word[1:]}{word[0]}ay"
    
    return f"{word}way"

def word_deconverter(word):
    if word[-3:] == "way":
        return word[:-3]

    return f"{word[-3:-2]}{word[:-3]}"

def pig_latin(text, option):
    text = text.lower().split()

    function = word_deconverter if option == 2 else word_converter
    words = list(map(function, text))

    return " ".join(words)

def main():
    print("Pig Latin Converter".center(50))
    print("*" * 50)
    
    print("1. To Pig Latin")
    print("2. From Pig Latin")
    print("3. Exit")

    option = int(input("Choose an option: "))
    if option == 3:
        return 
    
    print("*" * 50)
    text = input("Insert text to convert: ")
    print("*" * 50)
    return pig_latin(text, option)


if __name__ == "__main__":
    final = main()
    print("Converted Text:", "*" * 50, final, sep="\n")