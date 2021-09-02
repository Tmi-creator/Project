from random import randint
class Rogue(Unit): 
    def take_damage(dmg):
        if(randint(1,100) > self.first_skill):
            self.hp -= dmg
        else:
            print('Dodged:)')
            
    def take_damaged(dmg):
        if(randint(1,100) > self.first_skill // 3):
            self.hp -= dmg
        else:
            print('Dodged :)')
            
    def blades_of_death(target):
        if(self.mana >= 10):
            if(randint(1,100) > self.second_skill):
                attack(target)
                attack(target)                
            else:
                attack(target)
            self.mana -= 10            
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)
        
    def no_weapon(target):
        if(self.mana >= 10):
            target.cur_atk -= randint(1,self.third_skill)
            self.mana -= 10            
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)
        
class Paladin(Unit): # armor healer
        
    def take_damage(dmg):
        self.hp -= dmg + first_skill 
    
    def heal(target):
        if(self.mana >= 10):
            target.hp += second_skill
            if(target.hp > target.max_hp):
                target.hp = target.max_hp
            self.mana -= 10
            
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)
    
    def help_of_god(target):
        target.first_skill += self.third_skill
        target.second_skill += self.third_skill
        self.mana -= 10 * 3
