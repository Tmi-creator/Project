import self

from Unit import Unit


# class Hunter(Unit):  # summoner sniper (chto ya delayu voobche)
#
#     self.skills = {
#         1: self.attack,
#         2: self.first_skill,
#         3: self.second_skill,
#         4: self.third_skill
#     }
#
#     pass


# class Hunter_summons(Unit):
#     self.skills = {
#         1: self.attack,
#         2: self.first_skill,
#         3: self.second_skill,
#         4: self.third_skill
#     }
#
#     pass


class Warlock(Unit):  # мазохист dd (Много, очень очень много) (can heal himself)
    self.hp = 150
    self.atk = 20
    self.mana = 200
    self.first_skill_num = 1.1
    self.second_skill_num = 20
    self.third_skill_num = 30

    self.skills = {
        1: self.attack,
        2: self.first_skill,
        3: self.second_skill,
        4: self.third_skill
    }

    def first_skill(target):
        def suicide_mission():
            if self.hp > 1 and self.mana >= 10:
                ch = int(input())
                if ch > self.hp:
                    target.hp -= self.hp * self.first_skill_num
                    self.hp = 1
                else:
                    target.hp -= ch * self.first_skill_num
                    self.hp = -ch
            else:
                print("No mana!")
                target.attack(0.5 * self.cur_atk)


def second_skill(target):
    def masochizm():
        if self.hp > 20 and self.mana >= 10:
            target.take_damage(20 + self.second_skill_num)
            self.hp -= 20
        else:
            print("no hp/mana")
            target.attack(0.5 * self.cur_atk)


def third_skill(target):
    def take_hp():
        if self.mana >= 10:
            target.hp -= self.third_skill_num
            self.hp += self.third_skill_num - 10
            self.mana -= 10
        else:
            print("No mana!")
            target.attack(0.5 * self.cur_atk)
