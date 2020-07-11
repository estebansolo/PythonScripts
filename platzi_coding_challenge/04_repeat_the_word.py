def repeat_recursion(word, times):
    if times == 0:
        return ""

    return word + repeat_recursion(word, times - 1)

def main():
    word = input("Add the word you want to repeat: ")
    n_times = int(input("How many times you want to repeat the word? "))

    repeated_word = repeat_recursion(word, n_times)
    print(f"The final word is {repeated_word}")

    # Using Python Operators
    print(f"Python Operators: {word * n_times}")


if __name__ == "__main__":
    main()