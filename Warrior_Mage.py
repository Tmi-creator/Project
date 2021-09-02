from random import randint
class Warrior(Unit): # armor dd
    def take_damage(dmg):
        self.hp -= dmg + first_skill

    def simple_skill(target): #
        if(self.mana >= 10):
            target.take_damage(self.second_skill + self.atk * 0.5)
            self.mana -= 10

    def kill_rogue(target): #
        if(self.mana >= 10):
            if(target == Rogue):
                target.take_damaged(self.third_skill)
                target.take_damaged(self.third_skill)
                self.mana -= 10

class Mage(Unit): # super dd
    def total_annigilation(target):
        if(self.mana >= 10):
            target.take_damage(self.first_skill * randint(0,1) * randint(0,1) * randint(0,1) * randint(0,1) * randint(0,1))
            self.mana -= 10

    def buff(target):
        if(self.mana >= 10):
            target.atk += second_skill
            self.mana -= 10

    def mana_up(target):
        if(self.mana >= 10):
            target.mana += third_skill-10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)

