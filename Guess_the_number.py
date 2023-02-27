## Making a "Guess the number " game


# def input() - user input
# def num_guesses() -  number of num_guesses
# randomn_number_generator - Generate the randomn number
# game_handler() - Check if the number is higher , lower or same.
# def new_game()
# def check_wininer()
# def check_game_over()
# def try_again()

import random

user_guess  =  None
gameplay = None
correct_number =  None
num_of_guesses = 0


def new_game():
    """ The game should start with a banner printing banner """
    global user_guess,num_of_guesses
    gameplay = True
    # The gameplay should be a loop and check if we have a winner or gam-over
    while gameplay:
        print("|    " \
            "+++++++ This is a new game of 'Guess the number' +++++++"
            "   |" \
            )
        user_name = input("Enter your name?")

        # Fucntion for return the number of guesses
        num_of_guesses = num_guesses()
        print(" You have " + str(num_of_guesses) + " number of guesses")

        # Randomn number generator
        correct_number = random_number_generator(1,10)
        print("Computer automated number is" + str(correct_number))

        while num_of_guesses :
            user_guess =  users_guess()
            num_of_guesses -= 1
            # print(user_guess,num_of_guesses)

            game_handler()
            if num_of_guesses == 0:
                break
        continue_game = input("Do you want to try again ? a) Yes b) No ")
        if continue_game == "No" or "N":
            gameplay = False
            break
        elif continue_game == "Yes" or "Y":
            print(gameplay)
            new_game()


def num_guesses():
    global num_of_guesses
    num_of_guesses  = int(input("Define the number of guesses ,  Easy - 10 , Normal - 5 , Hard - 2"))
    return num_of_guesses


def users_guess():
    """Return the user guess number and the counter"""
    global user_guess
    user_guess = int(input("Please guess your number"))
    # num_of_guesses -= 1
    return user_guess



def random_number_generator(x,y):
    """ Generates a randomn number in a given range of x,y """
    global correct_number
    correct_number = random.randrange(x,y)
    return correct_number


def game_handler():
    """ A game handler will check if the user has finished all the guesses, then check if there is a winner OR check if there is a loser"""
    global user_guess,correct_number

    if user_guess > correct_number :
        print("Guessed number is bigger than the correct number. No. of chances left is " + str(num_of_guesses))

    elif user_guess < correct_number :
        print("Guessed number is smaller than the correct number. No. of chances left is " + str(num_of_guesses))
    check_winner()
    check_game_over()


# check the winner
def check_winner():
    """ Check the winner of the game"""
    global user_guess,correct_number
    if user_guess == correct_number:
        print("WINNER , You guessed the right number " + str(user_guess))
    return

#Check game is over, if yes revive if the user wants to play the game again
def check_game_over():
    """ Check if the correct number was not guessed"""
    global user_guess,correct_number
    if user_guess != correct_number and num_of_guesses == 0:
        print("Game over")
    return



new_game()
