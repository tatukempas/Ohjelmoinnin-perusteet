import random
random.seed(1234)

ascii_art = {
    "rock": """
    _______
---'   ____)
      (_____ )
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

def options():
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")

def player_wins_over(player, bot):
    return (player == "rock" and bot == "scissors") \
        or (player == "paper" and bot == "rock") \
        or (player == "scissors" and bot == "paper")

def main():
    player_stats = {"wins":0, "losses":0, "draws":0}
    bot_stats = {"wins":0, "losses":0, "draws":0}

    print("Program starting.")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}! Your opponent is RPS-3PO.")
    print("Game starts...\n")

    choices = {"1":"rock", "2":"paper", "3":"scissors"}

    while True:
        options()
        choice = input("Your choice: ").strip()
        if choice == "0":
            break
        if choice not in choices:
            print("Invalid choice! Please choose 1, 2, 3, or 0.\n")
            continue

        player_choice = choices[choice]
        bot_choice = choices[str(random.randint(1,3))]

        print("\nRock! Paper! Scissors! Shoot!\n")
        print("#"*25)
        print(f"{player_name} chose {player_choice}.\n{ascii_art[player_choice]}")
        print("#"*25)
        print(f"RPS-3PO chose {bot_choice}.\n{ascii_art[bot_choice]}")
        print("#"*25)

        if player_choice == bot_choice:
            print(f"Draw! Both chose {player_choice}.\n")
            player_stats["draws"] += 1
            bot_stats["draws"] += 1
        elif player_wins_over(player_choice, bot_choice):
            print(f"{player_name} {player_choice} beats RPS-3PO {bot_choice}.\n")
            player_stats["wins"] += 1
            bot_stats["losses"] += 1
        else:
            print(f"RPS-3PO {bot_choice} beats {player_name} {player_choice}.\n")
            player_stats["losses"] += 1
            bot_stats["wins"] += 1

    print("\nResults:")
    print(f"{player_name} - wins ({player_stats['wins']}), losses ({player_stats['losses']}), draws ({player_stats['draws']})")
    print(f"RPS-3PO - wins ({bot_stats['wins']}), losses ({bot_stats['losses']}), draws ({bot_stats['draws']})")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
