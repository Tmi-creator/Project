from random import randint
import dataclasses
@dataclasses.dataclass
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

class Warrior(Unit): # armor dd

    def take_damage(dmg):
        self.hp -= dmg + first_skill

    def simple_skill(target): #
        if(self.mana>=10):
            target.take_damage(self.second_skill + self.atk * 0.5)
            self.mana -= 10

    def kill_rogue(target): #
        if(self.mana>=10):
            if(target == Rogue):
                target.take_damaged(self.third_skill)
                target.take_damaged(self.third_skill)
                self.mana -= 10

class Mage(Unit): # super dd

    def total_annigilation(target):
        if(self.mana>=10):
            target.take_damage(self.first_skill*randint(0,1)*randint(0,1)*randint(0,1)*randint(0,1)*randint(0,1))
            self.mana-=10

    def buff(target):
        if(self.mana>=10):
            target.atk+=second_skill
            self.mana-=10

    def mana_up(target):
        if(self.mana>=10):
            target.mana+=third_skill-10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)


class Rogue(Unit): 
    super().__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)
    
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
        if(self.mana>=10):
            if(randint(1,100)>self.second_skill):
                attack(target)
                attack(target)
                
            else:
                attack(target)
            self.mana-=10
            
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)
        
    def no_weapon(target):
        if(self.mana>=10):
            target.cur_atk-=randint(1,self.third_skill)
            self.mana-=10
            
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)
        
class Paladin(Unit): # armor healer
        
    def take_damage(dmg):
        self.hp -= dmg + first_skill 
    
    def heal(target):
        if(self.mana>=10):
            target.hp+=second_skill
            if(target.hp>target.max_hp):
                target.hp=target.max_hp
            self.mana-=10
            
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)
    
    def help_of_god(target):
        target.first_skill+=self.third_skill
        target.second_skill+=self.third_skill
        self.mana-=10*3

        
class Hunter(Unit): # summoner sniper (chto ya delayu voobche)

class Hunter_summons(Unit):
        
class Warlock(Unit): # мазохист dd (Много, очень очень много) (can heal himself)
    
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



class Goblin(Unit):
   
class Skelet_ar(Unit):

class Ork(Unit):

class Necro(Unit):
   
class Skelet_w(Unit):
        
print("Приветствую тебя, странник! Если желаешь сыграть в пвп, жми 1, если против мобов - 2.")
choice1 = int(input())
if(choice1 == 1):
    print("1 на 1(1), командное(2) или ффа(3)?")
    choice2 = int(input())
    if(choice2 == 1):
        print("Ну, да начнется бой!\nВыберете персонажа для битвы:\nВоин-1\nМаг-2\nРазбойник-3\nПаладин-4\nОхотник-5\nЧернокнижник-6\nШаман-7\nДруид-8\nЖрец-9\n")
        choice3 = int(input())
        
         choice4 = int(input())
        @dataclasses.dataclass
        class UnitInfo:
        hp: int
        ...

        units = {
            1: [Warrior, UnitsInfo(hp=..., ...), ...]
        }
            
        units = {
            1: [Warrior, (200,20,50,-10,40,15), Warrior.attack,Warrior.Simple_Skill,Warrior.For_Killing_Rogue],
            2: [Mage,(100,40,100,2048,10,15),Mage.totalAnnigilation,Mage.buff,Mage.manaUp],
            3: [Rogue,(50,60,50,75,50,10)],
            4: [Paladin,(150,15,75,-5,40,10),Paladin.attack,Paladin.heal,Paladin.HelpOfGod],
            5: [Hunter,(1,1,1,1,1,1)],
            6: [Warlock,(150,20,200,1,1,1)],
            7: [Shaman,(1,1,1,1,1,1)],
            8: [Druid,(1,1,1,1,1,1)],
            9: [Priest,(150,20,50,80,5,5),Priest.heal,Priest.holy_light,Priest.revive]
        }
        uinfo1 = units.get(vibor3)
        p1 = uinfo1[0](*uinfo1[1])  
        uinfo2 = units.get(vibor4)
        p2 = uinfo2[0](*uinfo2[1])  
        while(p1.hp!=0 or p2.hp!=0):
            print("p1 turn, 1 - обычная атака,\n 2 - использование 1 способности,\n 3 - использование второй способности, и\n 4 - использование 3 способности\n")
            print(p1.hp,p1.cur_atk,p1.mana,"- p1")
            print(p2.hp,p2.cur_atk,p2.mana,"- p2")
            
