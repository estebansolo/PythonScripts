import random

CASES = ["rock", "paper", "scissors"]

def rps(user_option):
    pc_option = random.choice(CASES)
    if user_option == pc_option:
        return "tie"

    if user_option == "rock":
        return "computer" if pc_option == "paper" else "user"

    if user_option == "paper":
        return "computer" if pc_option == "scissors" else "user"

    if user_option == "scissors":
        return "computer" if pc_option == "rock" else "user"

def main():
    for key, case in enumerate(CASES):
        print(f"{key + 1}. {case}")

    user_option = int(input("Choose an option: "))

    winner = rps(CASES[user_option - 1])
    print(f"The winner is the {winner}" if winner != "tie" else "There was a tie")

if __name__ == "__main__":
    main()