import os
from random import randint, choice

new_round = False
game_running = True
game_results = []
enemies = ["Rocket Team", "Freezer", "Madara", "Kira", "Aizen"]


def get_player_choice(player, monster):
    os.system("clear")

    print(
        "{p_name} ({p_health}) vs {m_name} ({m_health})".format(
            p_name=player["name"],
            p_health=player["health"],
            m_name=monster["name"],
            m_health=monster["health"],
        ).center(50),
        end="\n\n",
    )

    print("1. Attack")
    print("2. Heal")
    print("3. Finish Game", end="\n\n")

    return input("Please select an action: ")


def new_game_choice():
    os.system("clear")
    print("Welcome to the battle game".center(50), end="\n\n")

    print("1. New Game")
    print("2. Show results")
    print("3. Exit Game", end="\n\n")

    return input("Please select an action: ")


def calculate_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)


def game_ends(winner, counter):
    print(f"{winner['name']} won the game")

    game_results.append(
        {"name": winner["name"], "health": winner["health"], "rounds": counter}
    )


def reset_players():
    monster = {
        "name": choice(enemies),
        "attack_min": 11,
        "attack_max": 18,
        "health": 100,
    }

    player = {"name": "", "attack": 14, "heal": 15, "health": 100}

    return monster, player


def start_new_game():
    global new_round, game_running

    new_game_option = new_game_choice()
    if new_game_option == "1":
        return input("Enter player name: ")

    if new_game_option == "2":
        print_results()

    elif new_game_option == "3":
        if game_results:
            print_results(wait=False)

        print("Thanks for playing".center(50))
        new_round = game_running = False


def print_results(wait=True):
    if not game_results:
        print("There are not results to display.")

    else:
        os.system("clear")

        print("Last Results".center(50))
        print("-" * 50)
        print("{:20}{:20}{:20}".format("Winner", "Health", "Rounds"))
        print("-" * 50)

        for player_stat in game_results:
            print("{name:15}{health:10}{rounds:20}".format(**player_stat))

    print("")

    if wait:
        input("Please press Enter to continue...")


while game_running:
    counter = 0
    monster, player = reset_players()
    new_player_game = start_new_game()

    if new_player_game is not None and new_player_game:
        new_round = True
        player["name"] = new_player_game

    while new_round == True:
        counter += 1
        player_won = monster_won = False
        player_choice = get_player_choice(player, monster)

        if player_choice in ["1", "2"]:
            if player_choice == "1":
                monster["health"] -= player["attack"]
            else:
                player["health"] += player["heal"]

            if monster["health"] <= 0:
                player_won = True

            else:
                player["health"] -= calculate_monster_attack(
                    monster["attack_min"], monster["attack_max"]
                )
                if player["health"] <= 0:
                    monster_won = True

            if player_won or monster_won:
                winner = player if player_won else monster
                game_ends(winner, counter)
                new_round = False

        elif player_choice == "3":
            game_ends(monster, counter)
            new_round = False
