import random

def launch_game():

    #computer selects a number from 1-10 randomly, player choice initialized
    options = [1,2,3,4,5,6,7,8,9,10]

    comp_choice = random.choice(options)
    player_choice = 0

    while player_choice != comp_choice:
        player_choice = int(input("Select a number from 1-10 \n"))
        if player_choice < comp_choice:
            print("Higher")
            continue
        elif player_choice > comp_choice:
            print("Lower")
            continue
    print("Yes! The number was {}".format(comp_choice))
  
launch_game()