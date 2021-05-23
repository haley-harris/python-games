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
    return player_input


def play_game(rounds):

    # intialize score
    player_score = 0
    computer_score = 0

    rounds = int(rounds)

    for i in range(rounds):
        
        # stores player and computer choices
        player_choice = player_select()
        computer_choice = computer_select()

        # if user puts in incorrect choice or numbers
        if (player_choice not in ['rock', 'paper', 'scissors']):
            print('Not a choice, try again')

        # game logic
        if (player_choice == 'rock' and computer_choice == 'scissors'):
            print('You won')
            player_score += 1
        elif (player_choice == 'paper' and computer_choice == 'rock'):
            print('You won')
            player_score += 1
        elif (player_choice == 'scissors' and computer_choice == 'paper'):
            print('You won')
            player_score += 1
        elif (player_choice == computer_choice):
            print('It\'s a draw') 
        else:
            print('Computer\'s point')
            computer_score +=1

    print(f'''Your score: {player_score}\nComputer score: {computer_score}''')

play_game(5)