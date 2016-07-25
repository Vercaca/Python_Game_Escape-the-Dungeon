import random
import role
import game
import sys
# random the pos of the three main items
# random pos of monster
posMonster = random.randrange(0, 9)

# random pos of exit
while True:
    posExit = random.randrange(0, 9)
    if posExit != posMonster:
        break

# random pos of player
while True:
    posPlayer = random.randrange(0, 9)
    if posPlayer != posMonster and posPlayer != posExit:
        break


# create new game
myGame = game.Game(posPlayer, posMonster, posExit)

# start game
while True:
    myGame.play()

    if myGame.end_game():
        break
