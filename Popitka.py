from random import randint

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

    def takeDamage(dmg):
        self.hp -= dmg

    def attack(target):
        target.takeDamage(self.atk)

class Warrior(Unit): # armor dd
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)

    def takeDamage(dmg):
        self.hp -= dmg + first_skill

    def Simple_Skill(target): #
        if(self.mana>=10):
            target.takeDamage(self.second_skill + self.atk * 0.5)
            self.mana -= 10

    def For_Killing_Rogue(target): #
        if(self.mana>=10):
            if(target == Rogue):
                target.takeDamageN(self.third_skill)
                target.takeDamageN(self.third_skill)
                self.mana -= 10

class Mage(Unit): # super dd
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)

    def totalAnnigilation(target):
        if(self.mana>=10):
            target.takeDamage(self.first_skill*(randint(0,1)*randint(0,1)*randint(0,1)*randint(0,1)*randint(0,1)))
            self.mana-=10

    def buff(target):
        if(self.mana>=10):
            target.atk+=second_skill
            self.mana-=10

    def manaUp(target):
        if(self.mana>=10):
            target.mana+=third_skill-10
        else:
            print('No mana!')
            target.takeDamage(self.atk * 0.5)


class Rogue(Unit): # break dance dd (poison, debuff)
# '''
# poison_skill = 0.05

# enemy.current_hp * (1 - poison_skill)


# '''
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)
    def takeDamage(dmg):
        if(randint(1,100) > self.first_skill):
            self.hp -= dmg
        else:
            print('Dodged:)')
    def takeDamageN(dmg):
        if(randint(1,100) > self.first_skill // 3):
            self.hp -= dmg
        else:
            print('Dodged :)')
            
    def bladesOfDeath(target):
        if(self.mana>=10):
            if(randint(1,100)>self.second_skill):
                attack(target)
                attack(target)
            else:
                attack(target)
            self.mana-=10
        else:
            print('No mana!')
            target.takeDamage(self.atk * 0.5)
        
    def noWeapon(target):
        if(self.mana>=10):
            target.cur_atk-=randint(1,self.third_skill)
            self.mana-=10
        else:
            print('No mana!')
            target.takeDamage(self.atk * 0.5)
        
class Paladin(Unit): # armor healer
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)
        
    def takeDamage(dmg):
        self.hp -= dmg + first_skill 
    
    def heal(target):
        if(self.mana>=10):
            target.hp+=second_skill
            if(target.hp>target.max_hp):
                target.hp=target.max_hp
            self.mana-=10 
        else:
            print('No mana!')
            target.takeDamage(self.atk * 0.5)
    
    def HelpOfGod(target):
        target.first_skill+=self.third_skill
        target.second_skill+=self.third_skill
        self.mana-=10*3

        
class Hunter(Unit): # summoner sniper (chto ya delayu voobche)
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)



class Hunter_summons(Unit):
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)
        
class Warlock(Unit): # мазохист dd (Много, очень очень много) (can heal himself)
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)

class Shaman(Unit): # totem dd healer
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)

    #def summon_attack_totem():
     #   pass

class Druid(Unit): # transformer dd healer
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)

class Priest(Unit): # super healer (can revive)
    def __init__(self, hp, atk,  mana, first_skill, second_skill, third_skill):
        Unit.__init__(self, hp, atk,  mana, first_skill, second_skill, third_skill)

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
                target.takeDamage(self.atk * 0.5)
                target.third_skill -= second_skill
                # добавить дебафф second_skill готово
        else:
            print('No mana!')
            target.takeDamage(self.atk * 0.5)


    def revive(target):
        if (self.mana >= 10):
            target.max_hp+=self.third_skill
            if (target.hp <= 0):
                target.hp = target.max_hp * 0.5
            else:
                target.hp = target.max_hp
        else:
            print('No mana!')
            target.takeDamage(self.atk * 0.5)



class goblin(Unit):
    def __init__(self, hp, atk, cur_atk):
        Unit.__init__(self, hp, atk, cur_atk)
   
class skelet_ar(Unit):
    def __init__(self, hp, atk, cur_atk):
        Unit.__init__(self, hp, atk, cur_atk)

class ork(Unit):
    def __init__(self, hp, atk, cur_atk):
        Unit.__init__(self, hp, atk, cur_atk)

class necro(Unit):
    def __init__(self, hp, atk, cur_atk):
        Unit.__init__(self, hp, atk, cur_atk)
   
class skelet_w(Unit):
    def __init__(self, hp, atk, cur_atk):
        Unit.__init__(self, hp, atk, cur_atk)
        
print("Приветствую тебя, странник! Если желаешь сыграть в пвп, жми 1, если против мобов - 2.")
vibor1 = int(input())
if(vibor1 == 1):
    print("1 на 1(1), командное(2) или ффа(3)?")
    vibor2 = int(input())
    if(vibor2 == 1):
        print("Ну, да начнется бой!\nВыберете персонажа для битвы:\nВоин-1\nМаг-2\nРазбойник-3\nПаладин-4\nОхотник-5\nЧернокнижник-6\nШаман-7\nДруид-8\nЖрец-9\n")
        vibor3 = int(input())
#         if(vibor3==1):
#             p1=Warrior(200,20,50,-10,40,15)
#         elif(vibor3==2):
#             p1=Mage(100,40,100,2048,10,15)
#         elif(vibor3==3):
#             p1=Rogue(50,60,50,75,50,10)
#         elif(vibor3==4):
#             p1=Paladin(150,15,75,-5,40,10)
#         elif(vibor3==5):
#             p1=Hunter()
#         elif(vibor3==6):
#             p1=Warlock()
#         elif(vibor3==7):
#             p1=Shaman()
#         elif(vibor3==8):
#             p1=Druid()
#         elif(vibor3==9):
#             p1=Priest(150,20,50,80,5,5)
#         print("Отличный выбор!\nИ второй игрок: ")
         vibor4 = int(input())
#         if(vibor4==1):
#             p2=Warrior(200,20,50,-10,40,15)
#         elif(vibor4==2):
#             p2=Mage(100,40,100,2048,10,15)
#         elif(vibor4==3):
#             p2=Rogue(50,60,50,75,50,10)
#         elif(vibor4==4):
#             p2=Paladin(150,15,75,-5,40,10)
#         elif(vibor4==5):
#             p2=Hunter()
#         elif(vibor4==6):
#             p2=Warlock()
#         elif(vibor4==7):
#             p2=Shaman()
#         elif(vibor4==8):
#             p2=Druid()
#         elif(vibor4==9):
#             p2=Priest(150,20,50,80,5,5)
        
            
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
            t1=int(input())
            if(t1 == 1):
                p1.attack(p2)
            elif(t1 == 2):
                print(uinfo1[2])
            elif(t1==3):
                uinfo1[3](p2)
            elif(t1 == 4):
                uinfo1[4](p2)
            print("p2 turn")
            t2=int(input())
            if(t2 == 1):
                p2.attack(p1)
            elif(t2 == 2):
                uinfo2[2](p1)
            elif(t2==3):
                uinfo2[3](p1)
            elif(t2 == 4):
                uinfo2[4](p1)
                


