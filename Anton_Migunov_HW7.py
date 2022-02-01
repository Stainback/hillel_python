"""
Написать игру "Угадай число". Написать программу, которая "загадает" рандомное число от 1 до n.
    Есть 2 (и больше) учасников, которые должны отгадать это число, если число отгадано - выводить
    имя участника и попытку, с которой он отгадал число.
Правила:
 - писать все функциями
 - обязательно запускать код для проверки!
 - число загадывается 1 раз на все время исполнения программы
 - количество попыток устанавливать сомостоятельно
"""
from numpy import random as npr


def set_participants(quantity: int) -> list:
    if quantity <= 2:
        print("Number of players has been set to 2 due to min quantity limitation.")
        return [1, 2]
    return [player for player in range(1, quantity+1)]


def main():
    # Initialize game properties
    players_quantity = input("Set number of players (min - 2 players): ")
    game_border = input("Set a limit for randomizer (integer positive number): ")

    # Validation
    if all((players_quantity.isdigit(), game_border.isdigit())):

        # Initialize game
        game_players = set_participants(int(players_quantity))
        goal_number = npr.randint(1, game_border)

        # Game loop
        turn = 1
        total_guesses_count = 0
        game = True
        while game:
            print(f"\n\tTurn {turn}: ")
            for player in game_players:

                player_guess = input(f"Now is your turn, player {player}. Make a guess: ")

                if player_guess.isdigit():
                    if int(player_guess) == goal_number:
                        print(f"You are right! Winner is player {player}."
                              f" All players made {total_guesses_count+1} guesses")
                        game = False
                        break
                    elif int(player_guess) > goal_number:
                        print("Your guess is bigger than goal number.")
                        total_guesses_count += 1
                    else:
                        print("Your guess is smaller than goal number.")
                        total_guesses_count += 1
                else:
                    print("You missed your turn! Next time enter integer number.")

            turn += 1

    else:
        raise ValueError


if __name__ == "__main__":
    main()
