import random

def launch_game():

    #computer selects a number from 1-10 randomly, player choice initialized

    comp_choice = random.randint(1,10)
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
