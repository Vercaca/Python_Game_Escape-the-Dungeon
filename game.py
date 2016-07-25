# this is a function
import sys
import role


class Game:
    def __init__(self, pos_player, pos_monster, pos_exit):

        self.pos_exit = pos_exit

        # create a player and a monster
        self.myPlayer = role.Player(pos_player)
        self.myMonster = role.Monster(pos_monster)

    # def play(self):
    #     # print(self, "posPlayer = ", self.myPlayer.pos, " , ", "posMonster = ", self.myMonster.pos, " , ", "posExit = "
    #     # , self.pos_exit, "\n")
    #     self.myPlayer.move()
    #     self.myMonster.move(self.pos_exit)

    def play(self, in_key):
        # print(self, "posPlayer = ", self.myPlayer.pos, " , ", "posMonster = ", self.myMonster.pos, " , ", "posExit = "
        # , self.pos_exit, "\n")
        self.myPlayer.move(in_key)
        self.myMonster.move(self.pos_exit)

    def end_game(self):
        if self.game_over():
            return True
        elif self.game_win():
            return True
        else:
            return False

    def game_over(self):
        if self.myPlayer.pos == self.myMonster.pos:
            print("||*** GameOver! You lose! ***                                 ||")
            return True
        else:
            self.print_main_menu()

            return False

    def game_win(self):
        if self.myPlayer.pos == self.pos_exit:
            print("||*** Congratulations!! You have found the EXIT! ***          ||")
            self.myMonster.face = "x﹏X"
            self.myPlayer.face = "^__^"
            return True
        else:
            return False

    def print_gui(self):
        pos_content = []
        for i in range(0, 9):
            pos_content.insert(i, "    ")

        pos_content[self.myPlayer.pos] = self.myPlayer.face
        if self.myMonster.visible:
            pos_content[self.myMonster.pos] = self.myMonster.face

        print("||\t\t==========================                    ||")
        print("||\t\t||", pos_content[0], "||", pos_content[1], "||", pos_content[2], "||                    ||")
        print("||\t\t||======================||                    ||")
        print("||\t\t||", pos_content[3], "||", pos_content[4], "||", pos_content[5], "||                    ||")
        print("||\t\t||======================||                    ||")
        print("||\t\t||", pos_content[6], "||", pos_content[7], "||", pos_content[8], "||                    ||")
        print("||\t\t==========================                    ||")
        print("||                                                            ||")
        print("||////////////////////////////////////////////////////////////||\n")


    @staticmethod
    def print_main_menu():
        print("||【Hints】Press [H] to get the hints (show/hide Monster)     ||")
        print("||【Move】 Press [a]->left / [d]->right / [w]->up / [s]->down ||")
        print("||............................................................||")
        # print("==============================================================")

