# This file is used to create the position of player
import random
import sys


class Role:
    def __init__(self, pos):
        self.pos = pos
        self.moveDict = {'left': -1, 'right': 1, 'up': -3, 'down': 3, 'none': 0}
        self.name = ""
        self.forbiddenPos = {'left': [0, 3, 6], 'right': [2, 5, 8], 'up': [0, 1, 2], 'down': [6, 7, 8], 'none': []}

    def get_next_pos(self, move_pos):
        new_pos = self.pos + self.moveDict[move_pos]    # count the movement

        print("(", self.name, "moves to ", new_pos, ")")
        return new_pos

    def set_pos(self, pos):
        self.pos = pos

    def correct_move(self, direction):
        if self.pos not in self.forbiddenPos[direction]:
            return True
        else:
            print("* Error: Try again! The direction cannot be '", direction, "' when currPos is ", self.pos)
            return False


class Monster(Role):
    def __init__(self, pos):
        super(Monster, self).__init__(pos)
        self.name = "Monster"
        self.visible = False

    def move(self, pos_exit):
        while True:
            ran_pos = random.choice(list(self.moveDict))

            if self.correct_move(ran_pos):
                # print("* monster's ran_pos = ", ran_pos)
                next_pos = self.get_next_pos(ran_pos)
                if next_pos != pos_exit:
                    self.set_pos(next_pos)
                    break


class Player(Role):
    def __init__(self, pos):
        super(Player, self).__init__(pos)
        self.visible = True
        self.name = "Player"
        self.key_to_direction = {'a\n': 'left', 'd\n': 'right', 'w\n': 'up', 's\n': 'down'}

    def move(self):
        while True:
            print("\n> Please input your movement  ( *tips a: left / d: right / w: up / s: down )")
            in_key = sys.stdin.readline()

            if in_key in list(self.key_to_direction):
                temp_dir = self.key_to_direction[in_key]

                if self.correct_move(temp_dir):
                    # print("* player's next_direction = ", temp_dir)
                    next_pos = self.get_next_pos(temp_dir)
                    self.set_pos(next_pos)
                    break
            else:
                print("* Warning: Wrong typing!")
