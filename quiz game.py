print("welcome to my quiz game")

play = input("do you want to play? ")
 
if play.lower() != "yes":
    quit() 

print("okey! let's play:)")
score = 0
right = 0
answer = input("what does HTML stands for? ").lower()
if answer == "hyper text markup language":
    print("correct")
    score += 2
    right += 1
else:
    print("incorrect")

answer = input("what does CSS stands for? ").lower()
if answer == "casecading style sheet":
    print("correct")
    score += 1
    right += 1
else:
    print("incorrect")

answer = input("what does SQL stands for? ").lower()
if answer == "stuctured query language":
    print("correct")
    score += 1
    right += 1
else:
    print("incorrect")    

answer = input("what does OOP stands for? ").lower()
if answer == "object oriented programme":
    print("correct")
    score += 1
    right += 1
else:
    print("incorrect")

answer = input("who craeted python programme? ").lower()
if answer == "guido van rossum":
    print("correct")
    score += 2
    right += 1
else:
    print("incorrect")  

answer = input("when did python created? ").lower()
if answer == "1980":
    print("correct")
    score += 2
    right += 1
else:
    print("incorrect")  

answer = input("when did python launched? ").lower()
if answer == "1991":
    print("correct")
    score += 1
    right += 1
else:
    print("incorrect")  

print("you got " + str(right) +" quiz correct")
print("you got "+ str((score/10)*100) +" %")


