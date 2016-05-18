import random

def launch_game():

    #computer selects a number from 1-10 randomly, player choice initialized

    comp_choice = random.randint(1,10)
    player_choice = 0
    number_range = list(range(1,11))

    while player_choice != comp_choice:
        try:
            player_choice = int(input("Select a number from 1-10 \n"))
        except ValueError:
            print("That wasn't a number, fool. Try again.")
            continue
        
        if player_choice not in number_range:
            print("That's not a number between 1 and 10. Try again, fool.")
            continue
        elif player_choice < comp_choice:
            print("Higher")
            continue
        elif player_choice > comp_choice:
            print("Lower")
            continue
    print("Yes! The number was {}".format(comp_choice))
  
launch_game()
