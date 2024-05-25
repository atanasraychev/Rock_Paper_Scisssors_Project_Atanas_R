import random

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
    print("Player wins")
if computer_choice == computer_list[0] and player_choice == "Scissors":
    print("Computer wins")
elif computer_choice == computer_list[1] and player_choice == "Rock":
    print("Computer wins")
elif computer_choice == computer_list[1] and player_choice == "Scissors":
    print("Player wins")
elif computer_choice == computer_list[2] and player_choice == "Rock":
    print("Player wins")
elif computer_choice == computer_list[2] and player_choice == "Paper":
    print("Computer wins")
elif computer_choice == player_choice:
    print("Draw")
