from random import randint

import self

from Unit import Unit


class Shaman(Unit):  # totem dd healer Не будет такого класса, и все тут
    pass


class Druid(Unit):  # transformer dd healer
    self.hp = 75
    self.atk = 10
    self.mana = 50
    self.first_skill_num = 0
    self.second_skill_num = 0
    self.third_skill_num = 0

    def first_skill(target):
        def transform():
            cooldown = 0
            if self.mana >= 10 and cooldown < 1:
                self.cur_atk += 30
                self.hp += 100
                self.max.hp = self.hp
                self.mana -= 10
                cooldown = 20
            else:
                print('No mana/cooldown!')
                target.take_damage(self.atk * 0.5)

    def second_skill(target):
        def dance_with_tambourine():
            if self.mana >= 10:
                if randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0, 1) == 1:
                    target.hp = 0
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)

    def third_skill(target):
        def revive():
            if self.mana >= 10:
                self.hp = 50
                self.cur_atk = 90
                self.mana = 0
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)


class Priest(Unit):  # super healer (can revive)
    self.hp = 150
    self.atk = 20
    self.mana = 50
    self.first_skill_num = 80
    self.second_skill_num = 5
    self.third_skill_num = 5

    def first_skill(target):
        def heal():
            if self.mana >= 10:
                target.hp += self.cur_atk * self.first_skill_num
                if target.hp > target.max_hp:
                    target.hp = target.max_hp
                self.mana -= 10
            # + buff first_skill готово
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)

    def second_skill(target):
        def holy_light():
            if self.mana >= 10:
                self.mana -= 10
                if target.third_skill_num == 'CREATURE':
                    target.hp - 1000
                else:
                    target.take_damage(self.atk * 0.5)
                    target.third_skill_num -= self.second_skill_num
                    # добавить дебафф second_skill готово

            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)

    def third_skill(target):
        def revive():
            if self.mana >= 10:
                target.max_hp += self.third_skill_num
                if target.hp <= 0:
                    target.hp = target.max_hp * 0.5
                else:
                    target.hp = target.max_hp
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)
