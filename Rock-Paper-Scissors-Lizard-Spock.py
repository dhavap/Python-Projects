# Rock Paper Scissors Lizard Spock

import random
from time import sleep

def rules():  #rules of the game
    gameRules = ('Scissors cuts paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock', 'Spock vaporises Rock', 'Rock crushes Scissors')
    for line in gameRules:
        print(line)
        sleep(1)

def game_play():  #Rock-Paper-Scissors-Lizard-Spock Game play
    # 0:scissors, 1:paper, 2:rock, 3:lizard, 4:spock 
    options = ("scissors", "paper", "rock", "lizard", "spock") 

    getRandomNum = random.randrange(0,4,1)  #computer selection
    print("\nLet\'s play! 1, 2, 3, GO!\n")
    sleep(0.5)
    while True:
        userSelection = (input('Your choice: ')).lower()
        if userSelection not in options:
            print('\nI\'m sorry! That is not a valid option. Type: scissors, paper, rock, lizard or spock.\nTry again!\n')
            continue
        else:
            break
    print('     VS\nComputer\'s choice:', (options[getRandomNum]).upper()) #user selection
    sleep(1)

    compWins = "Computer wins!\n"
    userWins = "User wins!\n"
    if userSelection == options[getRandomNum]: # tie
        print('It\'s a tie!')
    elif getRandomNum == 0: #comp choice = scissors
        if userSelection == options[1] or userSelection == options[3]:  #user chose paper or lizard
            print(compWins)
        else:
            print(userWins)
    elif getRandomNum == 1: #comp choice = paper
        if userSelection == options[2] or userSelection == options[4]: #user chose rock or spock
            print(compWins)
        else:
            print(userWins)
    elif getRandomNum == 2: #comp choice = rock
        if userSelection ==options[3] or userSelection == options[0]: #user chose lizard or scissors
            print(compWins)
        else:
            print(userWins)
    elif getRandomNum == 3: #comp choice = lizard
        if userSelection == options[1] or userSelection == options[4]:  #user chose paper or spock
            print(compWins)
        else:
            print(userWins)
    elif getRandomNum == 4: #comp choice = spock
        if userSelection == options[2] or userSelection == options[0]: #user chose rock or scissors
            print(compWins)
        else:
            print(userWins)
    sleep(1)



# BEGINNNING OF THE GAME
def start_game():
    print('Hi there!')
    sleep(1)
    print('Let\'s play a game!')
    sleep(1)
    userInput = (input('To play \'Rock-Paper-Scissors-Lizard-Spock\' say Y! To exit, say N. ')).lower()
    while True:
        if userInput == 'y':
            print('Great! First, let\'s talk about the rules.')
            while True:  # To view rules
                userInputGameRules = (input('Would you like to take a look at them? Y/N ')).lower()
                if userInputGameRules == 'y':
                    rules()
                    break
                elif userInputGameRules == 'n':
                    break
                else: 
                    print('I\'m sorry, did you mean Y/N ?')
            game_play()
            userInput = (input('Would you like to play again? Y/N ')).lower()
        elif userInput =='n':
            print(':( Bye! See you again soon!')
            break
        else:
            print('Invalid input. I don\'t understand what you mean. Let\'s try this again.')
            continue
    

###################################################################################################

start_game()

