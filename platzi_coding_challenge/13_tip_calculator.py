
def main():
    print("Tip Calculator".center(50))
    print("*" * 50)

    print("Enter the amounts you want, to finish leave empty")

    counter = 1
    prices = []
    while True:
        try:
            user_input = input(f"{counter}. Price: ")
            user_input = user_input.replace("$", "").strip()

            if user_input == "":
                break
            
            price = float(user_input)
        except:
            print("Invalid value, please try again")
        else:
            prices.append(price)
            counter += 1

    subtotal = sum(prices)
    tip = round(subtotal * 0.15, 2)

    print("*" * 50)
    print(f"Tip (15%): ${tip}")
    print(f"Order subtotal: ${subtotal}")
    print(f"Order total: ${subtotal + tip}")

if __name__ == "__main__":
    main()