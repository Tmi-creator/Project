
from random import randint
import dataclasses

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
    pass
class SkeletAr(Unit):
    pass
class Ork(Unit):
    pass
class Necro(Unit):
    pass
class SkeletWar(Unit):
    pass

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
            atk: int
            mana: int
            first_skill: int
            second_skill: int
            third_skill: int

        units = {
            1: [Warrior, UnitsInfo(hp = 200,atk = 20,mana = 50,first_skill = -10,second_skill = 40,third_skill = 15), Warrior.attack,Warrior.simple_skill,Warrior.kill_rogue]
            2: [Mage,UnitsInfo(hp = 100,atk = 40,mana = 100,first_skill = 2048,second_skill = 10,third_skill = 15),Mage.total_annigilation,Mage.buff,Mage.mana_up],
            3: [Rogue,UnitsInfo(hp = 50,atk = 60,mana = 50,first_skill = 75,second_skill = 50,third_skill = 10)],
            4: [Paladin,UnitsInfo(hp = 150,atk = 15,mana = 75,first_skill = -5,second_skill = 40,third_skill = 10),Paladin.attack,Paladin.heal,Paladin.help_of_god],
            5: [Hunter,UnitsInfo(hp = 150,atk = 15,mana = 75,first_skill = -5,second_skill = 40,third_skill = 10)],
            6: [Warlock,UnitsInfo(hp = 150,atk = 20,mana = 200,first_skill = 1,second_skill = 1,third_skill = 1)],
            7: [Shaman,UnitsInfo(hp = 150,atk = 15,mana = 75,first_skill = -5,second_skill = 40,third_skill = 10)],
            8: [Druid,UnitsInfo(hp = 150,atk = 15,mana = 75,first_skill = -5,second_skill = 40,third_skill = 10)],
            9: [Priest,UnitsInfo(hp = 150,atk = 20,mana = 50,first_skill = 80,second_skill = 5,third_skill = 5),Priest.heal,Priest.holy_light,Priest.revive]
        }
            

        uinfo1 = units.get(choice3)
        p1 = uinfo1[0](*uinfo1[1])  
        uinfo2 = units.get(choice4)
        p2 = uinfo2[0](*uinfo2[1])  
        while(p1.hp!=0 or p2.hp!=0):
            print("p1 turn, 1 - обычная атака,\n 2 - использование 1 способности,\n 3 - использование второй способности, и\n 4 - использование 3 способности\n")
            print(p1.hp,p1.cur_atk,p1.mana,"- p1")
            print(p2.hp,p2.cur_atk,p2.mana,"- p2")
        choices = {
            1:p1.attack(p2)
            2:p1.skill1(p2)
            3:p1.skill2(p2)
            4:p1.skill3(p2)
            5:p2.attack(p1)
            6:p2.skill1(p1)
            7:p2.skill2(p1)
            8:p2.skill3(p1)
        }
        t1 = int(input())
        t2 = int(input())
        choices.get(t1)
        choices.get(t2+4)
            
