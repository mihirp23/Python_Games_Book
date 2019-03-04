## Mihir Patel
## 3/4/19
## File : dragon_realm.py
## Python3

# Dragon Realm Game from Chapter 5
# In this game, the player is in a land full of dragons. The dragons all live
# in caves with their large piles of collected treasure. Some dragons are friendly
# and share their treasure. Other dragons are hungry and eat anyone who enters
# their cave. The player approaches two caves, one with a friendly dragon and 
# the other with a hungry dragon, but doesn't know which dragon is in which cave.
# The player must choose between the two.


import random
import time

#########################################################################
def displayIntro():
#########################################################################
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon 
is greedy and hungry, and will eat you on sight.''')
    print()

# displayIntro()

#########################################################################
def chooseCave():
#########################################################################
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave
# chooseCave()

#########################################################################
def checkCave(chosenCave):
#########################################################################
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and ...")
    print()
    time.sleep(2)
    friendlyCave = random.randint(1,2)
    
    if chosenCave == str(friendlyCave):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")
# checkWave()

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you want to play again? (yes or no)")
    playAgain = input()

