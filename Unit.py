class Unit(object):
    def __init__(self, hp, atk, mana, first_skill, second_skill, third_skill):
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.cur_atk = atk
        self.mana = mana
        self.first_skill = first_skill
        self.second_skill = second_skill
        self.third_skill = third_skill

    def take_damage(dmg):
        self.hp -= dmg

    def attack(target):
        target.take_damage(self.atk)
