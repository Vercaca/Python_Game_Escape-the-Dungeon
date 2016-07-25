# this is a function
import sys
import role


class Game:
    def __init__(self, pos_player, pos_monster, pos_exit):

        self.pos_exit = pos_exit
        # create a player and a monster
        self.myPlayer = role.Player(pos_player)
        self.myMonster = role.Monster(pos_monster)

    def play(self):
        print(self, "posPlayer = ", self.myPlayer.pos, " , ", "posMonster = ", self.myMonster.pos, " , ", "posExit = ",
              self.pos_exit)
        self.myPlayer.move()
        self.myMonster.move(self.pos_exit)
        print("-----------------------------------------------------\n")

    def end_game(self):
        if self.game_over():
            return True
        elif self.game_win():
            return True
        else:
            return False

    def game_over(self):
        if self.myPlayer.pos == self.myMonster.pos:
            print(self, "GameOver! You lose!")
            return True
        else:
            return False

    def game_win(self):
        if self.myPlayer.pos == self.pos_exit:
            print(self, "Congrats! You find the exit!")
            return True
        else:
            return False

    def __str__(self):
        return "【system】"

