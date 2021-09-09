class Hunter(Unit): # summoner sniper (chto ya delayu voobche)
        skills = {
        1:self.attack()
        2:self.first_skill()
        3:self.second_skill()
        4:self.third_skill()
        }
        pass
class Hunter_summons(Unit):
        skills = {
        1:self.attack()
        2:self.first_skill()
        3:self.second_skill()
        4:self.third_skill()
        }
        pass
class Warlock(Unit): # мазохист dd (Много, очень очень много) (can heal himself)
        self.hp=150
        self.atk=20
        self.mana=200
        
        skills = {
        1:self.attack()
        2:self.first_skill()
        3:self.second_skill()
        4:self.third_skill()
        }
