print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************        
''')

print('''Welcome to Treasure Island.
Your mission is to find the treasure. 
''')

choice1 = input("You arrived to an intersection. You have only 2 choices... 'right' or 'left' ! Write your choice : ")

if choice1 != "left":
    print("Game over ! You fall into a hole.")
    exit(1)

choice2 = input(''' Well Played ! Next you are in front of a lake. You have 2 choices... 
You can 'swim' or you can 'bypass'
What do you want to do ? ''')

if choice2 != "bypass":
    print("Game over ! You are attacked by a trout.")
    exit(1)

choice3 = input('''Congratulation ! 3 doors come up. "red", "blue", "yellow"...
Only one let you access to the treasure. Wich door will you choose ? ''')

if choice3 == "red":
    print("Game over ! You burn by fire.")
    exit(1)

elif choice3 == "blue":
    print("Game over ! You are eaten by beasts.")
    exit(1)

elif choice3 != "yellow":
    print("Game Over !")
    exit(1)

else:
    print("GGWP ! You Win !")
