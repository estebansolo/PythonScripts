import re
import os
import string
import getpass
from collections import defaultdict

new_round = False
game_running = True
game_results = defaultdict(list)

def print_results(wait=True):
    if not game_results:
        print("There are not results to display.")

    else:
        os.system("clear")

        print("Last Results".center(50))
        print("-" * 50)
        print("{:15}{:15}{:15}{:15}".format("Round", "Player", "Word", "Status"))
        
        for counter, players in game_results.items():
            print("-" * 50)
            for player in players:
                print("{:15}{:15}{:15}{:15}".format(counter, player["player"], player["word"], player["status"]))

    print("")

    if wait:
        input("Please press Enter to continue...")

def new_game_choice(active_players=False):
    os.system("clear")
    print("Welcome to the hangman game".center(50), end="\n\n")

    if active_players:
        print("0. Keep Players?")

    print("1. New Game")
    print("2. Show results")
    print("3. Exit Game", end="\n\n")

    return input("Please select an action: ")

def clear_word(word, chars):
    letters = set(list(string.ascii_lowercase))
    letters = list(letters - set(chars))

    word = word.lower()
    word = re.sub("|".join(list(map(lambda x: re.escape(x), list(string.punctuation)))), '', word)
    guess_word = " ".join(list(word))
    guess_word = re.sub("|".join(letters), '_', guess_word)
    return word, guess_word

def start_new_game(players):
    global new_round, game_running

    new_game_option = new_game_choice(players)
    if new_game_option == "0":
        return players

    if new_game_option == "1":
        return reset_players()

    if new_game_option == "2":
        print_results()
        pass

    elif new_game_option == "3":
        if game_results:
            print_results(wait=False)
            pass

        print("Thanks for playing".center(50))
        new_round = game_running = False

def reset_players():
    players_count = int(input("How many players?: "))

    players = []
    for i in range(players_count):
        name = input(f"Player {i + 1}: ")
        players.append(name)

    return players

def print_hangman(tries):
    current_hangman = {
        1: """
        --------
        |      |
        |      
        |     
        |     
        ---
        """,
        2: """
        --------
        |      |
        |      o
        |     
        |     
        ---
        """,
        3: """
        --------
        |      |
        |      o
        |      |
        |     
        ---
        """,
        4: """
        --------
        |      |
        |      o
        |      |\\
        |     
        ---
        """,
        5: """
        --------
        |      |
        |      o
        |     /|\\
        |     
        ---
        """,
        6: """
        --------
        |      |
        |      o
        |     /|\\
        |      \\
        ---
        """,
    }.get(tries, """
    --------
    |      
    |      
    |     
    |     
    ---
    """)

    print(current_hangman.center(50))

def get_player_round(player, counter):
    os.system("clear")

    tries = 0
    guess = ""
    status = "lose"
    max_tries = 7

    print(f"Round: {counter}")
    print(f"Player: {player}")

    while True:
        word = getpass.getpass("Please write a word or phrase to guess: ")
        word = word.strip()
        if len(word) > 5:
            break
        
        print("The word to guess must have at least 5 chars")

    word_tries = []

    while max_tries > tries:
        os.system("clear")

        word, guess = clear_word(word, word_tries)

        print(f"Round: {counter}")
        print(f"Tries: {tries}")
        print(f"Player: {player}", end="\n\n")

        print_hangman(tries)
        print(guess.center(50), end="\n\n")

        if word.replace(" ", "") == guess.replace(" ", ""):
            status = "won"
            print("Congratulations, You Won".center(50))
            break

        char = input("Please guess a letter: ")
        if char in word_tries:
            print("You already tried this one")
            input()
        else:
            word_tries.append(char)
            if char not in word:
                tries += 1
    else:
        print("Sorry, You Lose".center(50))

    input("Press any key to continue...")

    return {
        "word": word,
        "tries": tries,
        "status": status,
        "guess_word": guess
    }

def game_ends(round_id, player, stats):
    game_results[round_id].append({
        "player": player,
        **stats
    })

def main():
    global new_round

    counter = 0
    players = None

    while game_running:
        players = start_new_game(players)
        
        if players is not None and players:
            new_round = True

        while new_round:
            counter += 1
            for player in players:
                stats = get_player_round(player, counter)
                game_ends(counter, player, stats)

            new_round = False

if __name__ == "__main__":
    main()
