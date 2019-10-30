import random

class Character(object):

    def __init__(self,name, lvl):
        self.name = name
        self.lvl = lvl
        self.health = int(lvl/2*3/2)

    def block (self):
        randint = random.randint(1,20)
        if randint >15:
            return int(self.lvl/2*1.5/3)
        else:
            return 0
        
    def damage(self,dmg):
        block = self.block()
        if dmg-block < 0:
            dmg = 0
        else:
            dmg = dmg-block
            
        self.health -= dmg
        if (self.health <= 0):
            print("%s has lost %i health!" % (self.name, dmg))
            print("%s has died!\n" % self.name)
            return 1
        else:
            print("%s has lost %i health!\n" % (self.name, dmg))
            return 0
                  
        
    def attack(self):
        dmg = 0
        randint = random.randint(1,20)
        if randint > 15:
            dmg = self.lvl/4*1.5
            print ("%s's Attack Successful!" % self.name)
            
        else:
            print ("%s missed!" % self.name)
        return dmg


def win(char1, char2):
    if(char1.health > char2.health):
        winner = char1.name
    else:
        winner = char2.name
    print("%s has won" % winner)


Tak = Character("Takezo", 15)
Zat = Character("Zatuichi", 15)

def fight(Char1, Char2):

    i = 0
    j = 0
    y = 0
    z = 0
        
    while i == j:
        i = random.randint(1,20)
        j = random.randint(1,20)

    if i > j:
        att_fir = Char1
        att_sec = Char2
    else:
        att_fir = Char2
        att_sec = Char1

    while y != 1 and z != 1:
            
        z = att_fir.damage(att_sec.attack())

        if z != 1:
            y = att_sec.damage(att_fir.attack())

    win(Tak, Zat)
       

fight(Tak, Zat)




