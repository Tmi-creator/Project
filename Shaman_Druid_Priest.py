class Shaman(Unit):  # totem dd healer Не будет такого класса, и все тут
    skills = {
        1:self.attack()
        2:self.first_skill()
        3:self.second_skill()
        4:self.third_skill()
    }
    pass

class Druid(Unit):  # transformer dd healer
    skills = {
        1:self.attack()
        2:self.first_skill()
        3:self.second_skill()
        4:self.third_skill()
    }
    cooldown = 0
    def first_skill():
        def transform(target):
            if (self.mana >= 10 && cooldown<1):
                self.cur_atk+=30
                self.hp+=100
                self.max.hp=self.hp
                self.first_skill_num=0
                self.second_skill_num=0
                self.third_skill_num=0
                self.mana-=10
                cooldown=20
            else:
                print('No mana/cooldown!')
                target.take_damage(self.atk * 0.5)
    
    def second_skill():
        def dance_with_tambourine(target):
            if (self.mana >= 10):
                if(randint(0,1)*randint(0,1)*randint(0,1)*randint(0,1)==1):
                    target.hp=0
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)

    def third_skill():
        def revive(target):
            if (self.mana >= 10):
                self.hp=50
                self.cur_atk=90
                self.mana=0
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)


class Priest(Unit):  # super healer (can revive)
    self.hp=150
    self.atk=20
    self.mana=50
    self.first_skill_num=80
    self.second_skill_num=5
    self.third_skill_num=5
    
    skills = {
        1:self.attack()
        2:self.first_skill()
        3:self.second_skill()
        4:self.third_skill()
    }
    def first_skill():
        def heal(target):
            if (self.mana >= 10):
                target.hp += self.cur_atk * self.first_skill_num
                if (target.hp > target.max_hp):
                    target.hp = target.max_hp
                self.mana -= 10
            # + buff first_skill готово
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)
    
    def second_skill():
        def holy_light(target):
            if (self.mana >= 10):
                self.mana -= 10
                if (target.third_skill_num == 'CREATURE'):
                    target.hp - 1000
                else:
                    target.take_damage(self.atk * 0.5)
                    target.third_skill_num -= self.second_skill_num
                    # добавить дебафф second_skill готово

            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)

    def third_skill():
        def revive(target):
            if (self.mana >= 10):
                target.max_hp += self.third_skill_num
                if (target.hp <= 0):
                    target.hp = target.max_hp * 0.5
                else:
                    target.hp = target.max_hp
            else:
                print('No mana!')
                target.take_damage(self.atk * 0.5)
