class Shaman(Unit): # totem dd healer
    
class Druid(Unit): # transformer dd healer

class Priest(Unit): # super healer (can revive)
   
    def heal(target):
        if (self.mana >= 10):
            target.hp += atk * first_skill
            if (target.hp > target.max_hp):
                target.hp = target.max_hp
            self.mana -= 10
        # + buff first_skill готово
        else:
            print('No mana!')
            target.takeDamage(self.atk * 0.5)

    def holy_light(target):
        if (self.mana >= 10):
            self.mana -= 10
            if (target.third_skill == 'CREATURE'):
                target.hp - 1000
            else:
                target.take_damage(self.atk * 0.5)
                target.third_skill -= second_skill
                # добавить дебафф second_skill готово
                
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)


    def revive(target):
        if (self.mana >= 10):
            target.max_hp+=self.third_skill
            if (target.hp <= 0):
                target.hp = target.max_hp * 0.5
            else:
                target.hp = target.max_hp
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)

