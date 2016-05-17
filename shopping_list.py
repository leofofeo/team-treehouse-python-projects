#create a shopping list that allows someone to add items one by one to it
#if someone types in 'HELP' we should display the commands available to them ('HELP', 'DONE', 'SHOW')
#'DONE' will finish the shopping list editing
#'SHOW' will show us all items currently in shopping list



def start_program():
    print("What do you want to add to your shopping list? Type 'HELP' to see more options, and 'DONE' to finish adding items to your list.")
    
    #start_shopping_list() returns the final shopping list
    final_shopping_list = '\n '.join(start_shopping_list())

    print("You're done. The items on your shopping list are:")
    print(final_shopping_list)    

def start_shopping_list():
    shopping_list = []
    
    while True:
        commands = ['DONE', 'HELP', 'SHOW']
        
        user_input = input("> ")
    
        if user_input not in commands:
            shopping_list.append(user_input)
            continue
        elif user_input == 'HELP':
            print("Type 'HELP' to see this message again. Type 'SHOW' to see the items in your list. Type 'DONE' to finish your list.")
            continue
        elif user_input == 'SHOW':
            shopping_list_string = '\n '.join(shopping_list)
            print("The items currently in your list are:")
            print(shopping_list_string)
            continue
        elif user_input == 'DONE':
            return shopping_list
            break
        
        

start_program()
