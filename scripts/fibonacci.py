def fibonacci(last_term=10):
    first_term = 1
    second_term = 1

    numbers = []
    while len(numbers) < last_term:
        numbers.append(first_term)

        temp_term = first_term
        first_term = second_term
        second_term = temp_term + second_term

    print(*numbers, sep=" -> ")

if __name__ == "__main__":
    last_term = int(input("Enter the fibonacci series term limit: "))
    fibonacci(last_term)