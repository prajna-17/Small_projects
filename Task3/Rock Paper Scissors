import random

def get_computer_choice():
    return random.choice(["Rock","Paper","Scissors"])

def winner(user,computer):
    if user == computer:
        return "Tie"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You win!!!"
    else:
        return "Computer wins!!!"

def game():
    while True:
        computer_choice=get_computer_choice()
        player_Choice=input("Enter Rock, Paper, Scissors or ('Quit' to Exit):").capitalize()
        if player_Choice.lower() == "quit":
            print("Thank You")
            break
        elif player_Choice.lower() not in ["rock","paper","scissors"]:
            print("Invalid choice")
            print("Try again")
            continue
    
        
        print(f"Computer chose: {computer_choice}")
        print(winner(player_Choice.lower(),computer_choice.lower()))
game()
