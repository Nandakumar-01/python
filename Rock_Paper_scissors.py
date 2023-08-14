import random

options = ["rock","paper","scissors"]

user_wins = 0
computer_wins = 0


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:").lower

    if user_input == "q":
        quit
    if user_input in options:
        random_number = random.randint(0,2)
        computer_pick = options[random_number]
        print ("computer picked",computer_pick + ".")
 
        if(user_input == "rock" and computer_pick == "scissors") or (user_input == "paper" and computer_pick == "rock") or (user_input == "scissors" and computer_pick == "paper"):

            print("you won!")
            user_wins +=1
    
        

        elif(user_input == "scissors" and computer_pick == "rock") or (user_input == "rock" and computer_pick == "paper") or (user_input == "paper" and computer_pick == "scissors"):

            print("you lost!")
            computer_wins += 1
        
        else:
            print("it' draw!")
    else:
        print("invalid input.please type rock,paper,or scissors.")
    


print("Final score _ you:",user_wins,"coputer:",computer_wins)
print("Goodbye") 