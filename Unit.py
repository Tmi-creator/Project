class Unit(object):
    def __init__(self, hp, atk, mana, first_skill, second_skill, third_skill):
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.cur_atk = atk
        self.mana = mana
        self.first_skill_num = first_skill_num
        self.second_skill_num = second_skill_num
        self.third_skill_num = third_skill_num
    
    skills = {
        1:self.attack()
        2:self.first_skill()
        3:self.second_skill()
        4:self.third_skill()
    }
    def take_damage(dmg):
        self.hp -= dmg

    def attack(target):
        target.take_damage(self.atk)
        
    def first_skill():
         raise Exception("Override me")
            
    def second_skill():
         raise Exception("Override me")
            
    def third_skill():
         raise Exception("Override me")
