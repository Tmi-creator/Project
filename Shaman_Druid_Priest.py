class Shaman(Unit):  # totem dd healer
    pass

class Druid(Unit):  # transformer dd healer
    pass

class Priest(Unit):  # super healer (can revive)
    self.hp=150
    self.atk=20
    self.mana=50
    self.first_skill=80
    self.second_skill=5
    self.third_skill=5
    
    def first_skill():
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
    
    def second_skill():
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

    def third_skill():
        def revive(target):
            if (self.mana >= 10):
                target.max_hp += self.third_skill
                if (target.hp <= 0):
                    target.hp = target.max_hp * 0.5
                else:
                    target.hp = target.max_hp
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)
