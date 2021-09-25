from random import randint

import self

from Unit import Unit


class Rogue(Unit):
    self.hp = 50
    self.atk = 60
    self.mana = 50
    self.first_skill_num = 75
    self.second_skill_num = 50
    self.third_skill_num = 10
    self.skills = {
        1: self.attack,
        2: self.first_skill,
        3: self.second_skill,
        4: self.third_skill
    }

    def first_skill(dmg):
        def take_damage():
            if randint(1, 100) > self.first_skill_num:
                self.hp -= dmg
            else:
                print('Dodged:)')

        def take_damaged(dmg):
            if randint(1, 100) > self.first_skill_num // 3:
                self.hp -= dmg
            else:
                print('Dodged :)')

    def second_skill(target):
        def blades_of_death():
            if self.mana >= 10:
                if randint(1, 100) > self.second_skill_num:
                    self.attack(target)
                    self.attack(target)
                else:
                    self.attack(target)
                self.mana -= 10
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)

    def third_skill(target):
        def no_weapon():
            if self.mana >= 10:
                target.cur_atk -= randint(1, self.third_skill_num)
                self.mana -= 10
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)


class Paladin(Unit):  # armor healer
    self.hp = 150
    self.atk = 15
    self.mana = 75
    self.first_skill_num = -5
    self.second_skill_num = 40
    self.third_skill_num = 10
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
        def heal():
            if self.mana >= 10:
                target.hp += self.second_skill_num
                if (target.hp > target.max_hp):
                    target.hp = target.max_hp
                self.mana -= 10
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)

    def third_skill(target):
        def help_of_god():
            target.first_skill_num += self.third_skill_num
            target.second_skill_num += self.third_skill_num
            self.mana -= 10 * 3
