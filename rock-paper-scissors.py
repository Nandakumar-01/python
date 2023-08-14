import random

def get_user_choice():
    user_choice = input("choose rock, paper, or scissors").lower
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("invalid choice.please choose rock,paper,or scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def detemine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "it's draw!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "you win!"
    else:
        return "computer wins!" 

def play_game():
    user_choice = get_user_choice()
    computer_choice  = get_computer_choice()
    
    print(f"you chose {user_choice},and the coputer chose {computer_choice}.")
    result = detemine_winner(user_choice,computer_choice)
    
    print(result)

play_game() 