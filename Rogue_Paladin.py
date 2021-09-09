from random import randint


class Rogue(Unit):
    self.hp=50
    self.atk=60
    self.mana=50
    self.first_skill_num=75
    self.second_skill_num=50
    self.third_skill_num=10
    
    def first_skill():
        def take_damage(dmg):
            if (randint(1, 100) > self.first_skill_num):
                self.hp -= dmg
            else:
                print('Dodged:)')

        def take_damaged(dmg):
            if (randint(1, 100) > self.first_skill_num // 3):
                self.hp -= dmg
            else:
                print('Dodged :)')

    def second_skill():
        def blades_of_death(target):
            if (self.mana >= 10):
                if (randint(1, 100) > self.second_skill_num):
                    attack(target)
                    attack(target)
                else:
                    attack(target)
                self.mana -= 10
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)
    
    def third_skill():
        def no_weapon(target):
            if (self.mana >= 10):
                target.cur_atk -= randint(1, self.third_skill_num)
                self.mana -= 10
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)


class Paladin(Unit):  # armor healer
    self.hp=150
    self.atk=15
    self.mana=75
    self.first_skill_num=-5
    self.second_skill_num=40
    self.third_skill_num=10
    
    def first_skill():
        def take_damage(dmg):
            self.hp -= dmg + first_skill_num

    def second_skill():
        def heal(target):
            if (self.mana >= 10):
                target.hp += second_skill_num
                if (target.hp > target.max_hp):
                    target.hp = target.max_hp
                self.mana -= 10
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)

    def third_skill():
        def help_of_god(target):
            target.first_skill_num += self.third_skill_num
            target.second_skill_num += self.third_skill_num
            self.mana -= 10 * 3
