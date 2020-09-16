
#Code for the game

print("\n\nMade by Anuja Barve", "\nLet's play Stone, Paper, Scissor")
lose= ("The computer Wins")
win= ("You Win")
score=0
draw=0
lives=3
computer_lives=3

import time
time.sleep(0.50)
print("loading...")
time.sleep(0.50)
print("loading...")
time.sleep(0.50)
start_menu = """

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     ___                  ______________     ______________     _______________     ____      ___                                            
    ¦   ¦                ¦              ¦   ¦              ¦   ¦               ¦   ¦    ¦    /   /                                           
 /------------------     ¦     ___      ¦   ¦  __________  ¦   ¦  _____________¦   ¦    ¦   /   /                                            
/            \     ¦     ¦    ¦   ¦     ¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦  /   /                                             
¦       ------------     ¦    ¦___¦   __¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦_/   /                                              
¦       ------------     ¦           \      ¦ ¦          ¦ ¦   ¦ ¦                 ¦         /                                               
¦            \     ¦     ¦    ¦\      \     ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦\   \                                               
¦       ------------     ¦    ¦ \      \    ¦ ¦__________¦ ¦   ¦ ¦_____________    ¦    ¦ \   \                                              
¦       ------------     ¦    ¦  \      \   ¦              ¦   ¦               ¦   ¦    ¦  \   \                   ___  ___  ___  ___    
¦           a
 \     ¦     ¦____¦   \______\  ¦______________¦   ¦_______________¦   ¦____¦   \___\                 ¦   ¦¦   ¦¦   ¦¦   ¦       
¦       ------------                                                                                          ___ ¦   ¦¦   ¦¦   ¦¦   ¦       
\       ------------ ____________    _______________     ___________     ___________     _____________       ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
 \           \     /¦   _____   ¦   ¦     _____     ¦   ¦   _____   ¦   ¦           ¦   ¦             ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
  \---------------/ ¦  ¦     ¦  ¦   ¦    ¦_____¦    ¦   ¦  ¦     ¦  ¦   ¦    _______¦   ¦     ___     ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦  ¦_____¦  ¦   ¦     _____     ¦   ¦  ¦_____¦  ¦   ¦   ¦           ¦    ¦   ¦    ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦    _______¦   ¦    ¦     ¦    ¦   ¦    _______¦   ¦   ¦_____      ¦    ¦___¦   _¦      \                       /       
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦    _____¦     ¦           \         \                     /        
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦   ¦_______    ¦    ¦\      \         \                   /         
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦           ¦   ¦    ¦ \      \         \                 /                                _____
                    ¦___¦           ¦____¦     ¦____¦   ¦___¦           ¦___________¦   ¦____¦  \______\         \_______________/                                /     /
                                                                                                                                                                 /     /
 ______________     _______________     ____     ______________     ______________     ______________     _____________     ______________                    /     /
¦   ___________¦   ¦               ¦   ¦    ¦   ¦   ___________¦   ¦   ___________¦   ¦              ¦   ¦             ¦   ¦   ___________¦    ________    /     /
¦  ¦               ¦  _____________¦   ¦    ¦   ¦  ¦               ¦  ¦               ¦  __________  ¦   ¦     ___     ¦   ¦  ¦               /          /     /
¦  ¦___________    ¦ ¦                 ¦    ¦   ¦  ¦___________    ¦  ¦___________    ¦ ¦          ¦ ¦   ¦    ¦   ¦    ¦   ¦  ¦___________   ¦         /     /
¦____________  ¦   ¦ ¦                 ¦    ¦   ¦____________  ¦   ¦____________  ¦   ¦ ¦          ¦ ¦   ¦    ¦___¦   _¦   ¦____________  ¦  ¦       /     /
             ¦ ¦   ¦ ¦                 ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦          ¦ ¦   ¦           \                  ¦ ¦  ¦               __________________
             ¦ ¦   ¦ ¦_____________    ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦__________¦ ¦   ¦    ¦\      \                 ¦ ¦  ¦                                 ¦
 ____________¦ ¦   ¦               ¦   ¦    ¦    ____________¦ ¦    ____________¦ ¦   ¦              ¦   ¦    ¦ \      \    ____________¦ ¦  ¦               __________________¦
¦______________¦   ¦_______________¦   ¦____¦   ¦______________¦   ¦______________¦   ¦______________¦   ¦____¦  \______\  ¦______________¦  ¦______________¦

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Game rules:

Stone looses against Paper
Stone beats Scissors
Paper beats Stone
Paper looses against Scissors
Scissors beats Paper
Scissors looses against Stone
---------------------------------------------------------
The computer has lives too, can you beat the computer ??
GOOD LUCK !!!!!!!
---------------------------------------------------------
"""
print(start_menu)
while True:
                sps = input("Stone, Paper, Scissor ?  ")
                sps = sps.title()
                import random
                computer = ("stone", "paper", "scissor")
                computer = random.choice(computer)

                #lives
                if lives == 0 :
                    print("Thanks for playing.")
                    print("You have run out of lives")
                    print("You got", score, "correct")
                    print("You drew", draw, "times")
                    stop = input("Press enter to exit.")
                    exit()
                if computer_lives == 0:
                    print("Thanks for playing.")
                    print("The computer lost all it's lives. You Win.")
                    print("You got", score, "correct")
                    print("You drew", draw, "times")
                    stop = input("Press enter to exit.")
                    exit()

                #if Stone statements:
                if sps== "Stone" and computer== "paper":
                    print("")
                    print("The computer choose", computer)
                    print(lose)
                    print("")
                    lives-=1
                if sps== "Stone" and computer== "scissor":
                    print("")
                    print("The computer choose", computer)
                    print(win)
                    computer_lives-=1
                    print("")
                    score+=1
                #if Paper statements:
                if sps== "Paper" and computer== "stone":
                    print("")
                    print("The computer choose", computer)
                    print(win)
                    computer_lives-=1
                    print("")
                    score+=1
                if sps== "Paper" and computer== "scissor":
                    print("")
                    print("The computer choose", computer)
                    print(lose)
                    print("")
                    lives-=1
                #if Scissor statements:
                if sps== "Scissor" and computer== "stone":
                    print("")
                    print("The computer choose", computer)
                    print(lose)
                    print("")
                    lives-=1
                if sps== "Scissor" and computer == "paper":
                    print("")
                    print("The computer choose", computer)
                    print(win)
                    computer_lives -= 1
                    print("")
                    score += 1
                # draw statements:
                if sps== "Stone" and computer=="stone":
                    print("")
                    print("The computer choose", computer)
                    print("It's a Draw")
                    print("")
                    draw+=1
                if sps == "Paper" and computer == "paper":
                    print("")
                    print("The computer choose", computer)
                    print("It's a Draw")
                    print("")
                    draw += 1
                if sps == "Scissor" and computer == "scissor":
                    print("")
                    print("The computer choose", computer)
                    print("It's a Draw")
                    print("")
                    draw += 1

                print("Your score is", score)
                print("Lives remaining: ", lives)

print("Thanks for playing..")