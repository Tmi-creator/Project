import self as self
from random import randint


class Enemy(object):
    def __init__(self, hp, atk, provocation):
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.cur_atk = atk
        self.provocation = provocation



