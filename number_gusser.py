import random

def guess_the_number():
    random_number = random.randint(1,100)
    
    attempts = 0

    print("welcom to the guess the number! ")
    print("choose a number between 1 to 100. try to guess it!")

    while True:
        guess = int(input("enter your guess: "))
        
        attempts += 1

        if guess == random_number:
            print(f"congratulations! you gussed the number {random_number} in {attempts} attempts.")
            break
        elif guess < random_number :
            print("too low.try again. ")
        else:
            print("too high. try again .")

'''if the script is run as a main programme ,the __name__ variable will have the vale  "__main__" this happens directly excite the programme stand alone.'''            

if __name__ == "__main__" :
    guess_the_number()          



  

