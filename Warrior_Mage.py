from random import randint


class Warrior(Unit):  # armor dd
    self.hp=200
    self.atk=20
    self.mana=50
    self.first_skill=-10
    self.second_skill=40
    self.third_skill=15
    
    def first_skill():
        def take_damage(dmg):
            self.hp -= dmg + first_skill
            
    def second_skill():
        def simple_skill(target):  #
            if (self.mana >= 10):
                target.take_damage(self.second_skill + self.atk * 0.5)
                self.mana -= 10

    def third_skill():
        def kill_rogue(target):  #
            if (self.mana >= 10):
                if (target == Rogue):
                    target.take_damaged(self.third_skill)
                    target.take_damaged(self.third_skill)
                    self.mana -= 10


class Mage(Unit):  # super dd
    self.hp=100
    self.atk=40
    self.mana=100
    self.first_skill=2048
    self.second_skill=10
    self.third_skill=15
    
    def first_skill():
        def total_annigilation(target):
            if (self.mana >= 10):
                target.take_damage(
                    self.first_skill * randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0, 1))
                self.mana -= 10

    def second_skill():
        def buff(target):
            if (self.mana >= 10):
                target.atk += second_skill
                self.mana -= 10

    def third_skill():
        def mana_up(target):
            if (self.mana >= 10):
                target.mana += third_skill - 10
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)
