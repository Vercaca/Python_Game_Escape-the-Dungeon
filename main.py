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


# welcome
print("\n||////////////////////////////////////////////////////////////||")
print("|| Welcome to \"Escape the Dungeon\"!                           ||")
print("|| There is a MONSTER chasing after YOU!                      ||")
print("|| Run and find the EXIT as soon as possible!                 ||")
print("||                                                            ||")

# create new game
myGame = game.Game(posPlayer, posMonster, posExit)

# show the GUI
myGame.print_main_menu()
myGame.print_gui()

# start game
while True:
    print("> Please input your movement:")
    in_key = sys.stdin.readline()
    if in_key == 'H\n':
        print("Give you a hint!")
        print("||////////////////////////////////////////////////////////////||")
        myGame.myMonster.visible = True
        myGame.print_gui()
        myGame.myMonster.visible = False
        in_key = ""

    myGame.play(in_key)

    print("||////////////////////////////////////////////////////////////||")
    if myGame.end_game():
        myGame.print_gui()
        break

    myGame.print_gui()
