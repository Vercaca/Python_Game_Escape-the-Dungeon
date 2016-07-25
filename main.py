import game
import sys


# welcome
print("\n||////////////////////////////////////////////////////////////||")
print("|| Welcome to \"Escape the Dungeon\"!                           ||")
print("|| There is a MONSTER chasing after YOU!                      ||")
print("|| Run and find the EXIT as soon as possible!                 ||")
print("||                                                            ||")

# create new game
myGame = game.Game()

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
        # break
        # restart?
        print("> Restart? (Y/N)")
        in_key = sys.stdin.readline()
        while in_key != "Y\n" and in_key != "N\n":
            print("> Restart? (Y/N)")
            in_key = sys.stdin.readline()

        if in_key == "Y\n":
            myGame = game.Game()
            # show the GUI
            myGame.print_main_menu()
            # myGame.print_gui()
        elif in_key == "N\n":
            print("> BYE BYE!")
            break

    myGame.print_gui()
