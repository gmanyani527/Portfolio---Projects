import random 



while True: 
    user_choice = input("Enter a choice(rock, paper, and scissors)")

    possiblea_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possiblea_actions)

    print (f"\nYou chose {user_choice}, computer chose {computer_action}.\n")

    if user_choice == computer_action:
        print(f"Both players selected{computer_action}. Its a tie" )
    elif user_choice == "rock":
        if computer_action == "paper": 
            print("Paper will cover the rock! You lose!")
        else: 
            print("Scissors are smashed by the rock! You win!")
    elif user_choice == "paper": 
        if computer_action == "scissors": 
            print("Scissors beat paper! You lose!")
        else: 
            print("Paper beats rock! You win.")
    elif user_choice == "scissors":
        if computer_action == "rock":
            print("Rock will beat scissors. You win")
        else: 
            print("Paper will cover rock! You lose")
    repeat = input("\nPlay again? (yes/no): ")
    if repeat.lower() != "yes":
        print("Thanks for playing!")
        break