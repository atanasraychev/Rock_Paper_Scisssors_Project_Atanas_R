from colorama import Fore, Back, Style
import random

game_restart = "Yes"

while game_restart == 'Yes':

    input_check = 1

    while input_check == 1:
        player_message = int(input(f'Choose from the list :  Rock, Paper or Scissors! \n'
                               '1 : Rock\n'
                               '2 : Paper\n'
                               '3 : Scissors\n'))

        if player_message == 1:
            player_choice = "Rock"
            input_check = 0
        elif player_message == 2:
            player_choice = 'Paper'
            input_check = 0
        elif player_message == 3:
            player_choice = "Scissors"
            input_check = 0
        else:
            print("Wrong choice! Try again - 1, 2 or 3 :)\n")

    computer_list = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(computer_list)

    print(f'Player\'s choice : {player_choice}')
    print(f'Computer\'s choice : {computer_choice}')

    if computer_choice == computer_list[0] and player_choice == "Paper":
        print(Fore.GREEN + "Player Wins")
    if computer_choice == computer_list[0] and player_choice == "Scissors":
        print(Fore.RED +"Computer wins")
    elif computer_choice == computer_list[1] and player_choice == "Rock":
        print(Fore.RED + "Computer wins")
    elif computer_choice == computer_list[1] and player_choice == "Scissors":
        print(Fore.GREEN + "Player wins")
    elif computer_choice == computer_list[2] and player_choice == "Rock":
        print(Fore.GREEN + "Player wins")
    elif computer_choice == computer_list[2] and player_choice == "Paper":
        print(Fore.RED + "Computer wins")
    elif computer_choice == player_choice:
        print(Fore.YELLOW + "Draw")

    print(Style.RESET_ALL)
    print("Do you want to play again? - Yes or No?")

    game_restart = input()

    if game_restart == 'No':
        break

print('Thanks for playing')
