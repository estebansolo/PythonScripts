
def prime_numbers(max_number):
    primes = []
    for number in range(1, max_number):
        for valid in range(2, (max_number // 2) + 1):
            if not number % valid and number != valid:
                break
        else:
            primes.append(number)

    return primes

def main():
    print("Primer Numbers".center(50))
    print("*" * 50)

    while True:
        try:
            max_number = int(input("Max number: "))
        except:
            print("There was an error")
        else:
            if max_number >= 1:
                break
            else:
                print("Number must be greater than 0")

    numbers = prime_numbers(max_number)
    print(*numbers, sep="\n")

if __name__ == "__main__":
    main()