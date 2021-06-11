#! python3

import random 


def computer_select():
    choice = ['rock', 'paper', 'scissors']
    # computer's randomized choice
    computer_choice = random.choice(choice)
    return computer_choice


def player_select():
    # prompt user for choice - converts input to lowercase
    player_input = input('Choose rock, paper, or scissors: ').lower()
    
    # if user puts in incorrect choice or ints
    if (player_input not in ['rock', 'paper', 'scissors']):
        print('Not a choice, try again')
        player_select()
    else:
        return player_input


def select_rounds():
    # validate user input is an integer with try except statement
    while True:
        try:
            # prompt user for number of rounds
            rounds = int(input('Number of rounds: '))
        except ValueError:
            print('Please enter a number')
            continue
        else:
            return rounds
            break


def play_game():
    # intialize scores
    player_score = 0
    computer_score = 0
    # set number of rounds
    rounds = select_rounds()
    
    for i in range(rounds):
        # stores player and computer choices
        player_choice = player_select()
        computer_choice = computer_select()

        # print computer's choice to screen
        print(f"\nComputer's choice: {computer_choice}\n")

        # game logic
        if player_choice == 'rock' and computer_choice == 'scissors':
            print('You won')
            player_score += 1
        elif player_choice == 'paper' and computer_choice == 'rock':
            print('You won')
            player_score += 1
        elif player_choice == 'scissors' and computer_choice == 'paper':
            print('You won')
            player_score += 1
        elif player_choice == computer_choice:
            print("It's a draw") 
        else:
            print("Computer's point")
            computer_score +=1

    print(f'\nYour score: {player_score}\nComputer score: {computer_score}')


if __name__ == '__main__':

    play_game()