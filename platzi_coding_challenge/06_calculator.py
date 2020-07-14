def calculator(num_a, operator, num_b):
    return {
        "+": num_a + num_b,
        "-": num_a - num_b,
        "/": num_a / num_b,
        "*": num_a * num_b,
    }.get(operator, "Invalid Operator")
    
def main():
    num_a = float(input("Please add the first number: "))
    
    while True:
        operator = input("Please add the operator: ")
        if operator in ["+", "-", "*", "/"]:
            break

        print("Invalid operator")

    num_b = float(input("Please add the second number: "))

    try:
        total = calculator(num_a, operator, num_b)
        print(f"The total of {num_a}{operator}{num_b} is {total}")
    except ZeroDivisionError:
        print("There is an error with the divisor.")

if __name__ == "__main__":
    main()