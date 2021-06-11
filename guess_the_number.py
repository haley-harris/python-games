import random
import sys


def print_intro():

    # print game instructions
    print('*' * 42)
    print('Can you guess the number in just 7 tries?\n * hint: min + max / 2')
    print('*' * 42 + '\n')

def print_numbers(min, max):

    # print list of numbers to screen for visualization
    num_list = list(range(min, max + 1))
    print(num_list)


def play_game():

    # print game intro/instructions
    print_intro()

    # set initial min and max vars
    min = 1
    max = 100 
    # set max number of rounds 
    # for an arr size of 100 -> 2^7 = 128 = 7 guesses max
    round_count = 7

    # print initial list of numbers
    print_numbers(min, max)

    # store target number
    target = random.randrange(1, 100)

    while round_count != 0:
        # have user guess number
        guess = int(input('\nguess the number: '))

        if guess < target:
            # if guess lower than target, guess + 1 becomes new min
            print('your guess was lower than the target number\n')
            min = guess + 1
            print_numbers(min, max)
            round_count -= 1
        elif guess > target:
            # if guess greater than target, guess - 1 becomes new max
            print('your guess was greater than the target number\n')
            max = guess - 1
            print_numbers(min, max)
            round_count -= 1
        elif guess == target:
            print(f'you got it! the correct number was {target}')
            break

    # ask if user wants to play again
    try_again = input('would you like to play again? y/n ')

    if try_again.lower() == 'y':
        play_game()
    else:
        sys.exit()


if __name__ == '__main__':

    play_game()