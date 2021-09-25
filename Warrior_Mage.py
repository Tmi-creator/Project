from random import randint

import self

from Rogue_Paladin import Rogue
from Unit import Unit


class Warrior(Unit):  # armor dd
    self.hp = 200
    self.atk = 20
    self.mana = 50
    self.first_skill_num = -10
    self.second_skill_num = 40
    self.third_skill_num = 15

    self.skills = {
        1: self.attack,
        2: self.first_skill,
        3: self.second_skill,
        4: self.third_skill
    }

    def first_skill(dmg):
        def take_damage():
            self.hp -= dmg + self.first_skill_num

    def second_skill(target):
        def simple_skill():  #
            if self.mana >= 10:
                target.take_damage(self.second_skill_num + self.atk * 0.5)
                self.mana -= 10

    def third_skill(target):
        def kill_rogue():  #
            if self.mana >= 10:
                if target == Rogue:
                    target.take_damaged(self.third_skill_num)
                    target.take_damaged(self.third_skill_num)
                    self.mana -= 10


class Mage(Unit):  # super dd
    self.hp = 100
    self.atk = 40
    self.mana = 100
    self.first_skill_num = 2048
    self.second_skill_num = 10
    self.third_skill_num = 15

    self.skills = {
        1: self.attack,
        2: self.first_skill,
        3: self.second_skill,
        4: self.third_skill
    }

    def first_skill(target):
        def total_annigilation():
            if self.mana >= 10:
                target.take_damage(
                    self.first_skill_num * randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0,
                                                                                                                   1))
                self.mana -= 10

    def second_skill(target):
        def buff():
            if self.mana >= 10:
                target.atk += self.second_skill_num
                self.mana -= 10

    def third_skill(target):
        def mana_up():
            if self.mana >= 10:
                target.mana += self.third_skill_num - 10
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)
