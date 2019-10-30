from Characters import player
from utilities import util



def Level(exp):
        new_exp = player.exp + exp
        player.exp = new_exp
        st_lvl=player.lvl
        
        if player.exp < 10:
            lvl = 1
        elif player.exp >= 10 and player.exp < 25:
            lvl = 2
        elif player.exp >= 25 and player.exp < 50:
            lvl = 3
        elif player.exp >= 50 and player.exp < 100:
            lvl = 4
        elif player.exp >= 100 and player.exp < 200:
            lvl = 5
        elif player.exp >= 200 and player.exp < 500:
            lvl = 6
        elif player.exp >= 500 and player.exp < 1000:
            lvl = 7
        elif player.exp <= 1000 and player.exp < 1500:
            lvl = 8
        elif player.exp >= 1500 and player.exp < 2000:
            lvl = 9
        elif player.exp >= 2000 and player.exp < 3000:
            lvl = 10
        else:
            lvl = 11

        if lvl > st_lvl:
            print("\n\n\t\t\tYou have levled up!\n\n")
            return lvl
        else:
            return lvl

#------------------------------------------------------------------------------

class weapon(object):
    weapon_name = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        weapon.objects[self.weapon_name] = self

    def attDie(self):
        dice = self.att_die
        return dice

    def dice(self):
        print("You chose: %s, for 1-%i damage." % (self.name, self.att_die))
        affirm = util.yesOrNo("Is this correct? (Y/N) >>  ")
        if affirm:
            return self.att_die
        else:
            return False  
        
    
class Paddle(weapon):
    def __init__(self, name, att_die, cost):
        self.weapon_name = "paddle"
        self.att_die = att_die
        self.cost = cost
        super().__init__(name)

            #    Name    att_die    cost
paddle = Paddle("paddle", 1000,   1000000)


class Stick(weapon):
   def __init__(self, name, att_die, cost):
        self.weapon_name = "stick"
        self.att_die = att_die
        self.cost = cost
        super().__init__(name)
    
            #    Name    att_die    cost
stick = Stick("stick",     3,        0)


class Fist(weapon):
   def __init__(self, name, att_die, cost):
        self.weapon_name = "fist"
        self.att_die = att_die
        self.cost = cost
        super().__init__(name)
    
        #    Name    att_die    cost
fist = Fist("fist",     2,        0)





"""          
kubaton = weapon("kubaton", 4, 5)         
knife = weapon("knife", 4, 5)
rusty_sword = weapon("rusty-sword", 5, 10)
short_sword = weapon("short-sword", 6, 50)
sword = weapon("sword", 8, 100)
tanto = weapon("tanto", 10, 300)
katana = weapon("katana", 15, 500)
jo-staff = weapon("jo-staff",  10, 150)
bo-staff = weapon("bo-staff",  12, 175)
"""


def weapInput(prompt):
    weapon = input(prompt)
    return weapon.strip()

def getWeapon():           
    tempWeap = "" 
                
    while True:
        tempWeap = weapInput("\nChoose your weapon. >> ")

                               
        if tempWeap in weapon.objects:
            charWeap = weapon.objects[tempWeap]
            weapDie = charWeap.dice()                
            if weapDie != False:
                return weapDie
            else:
                pass
        else:
            print("There is no " + tempWeap + " here. Choose anouther weapon")
            continue
        
           
def gameWeapon(weap):
        tempWeap = weap         
                                          
        if tempWeap in weapon.objects:
            charWeap = weapon.objects[tempWeap]
            weapDie = charWeap.dice()                
            if weapDie != False:
                return weapDie
            else:
                pass
        else:
            print("There is no " + tempWeap + " here. Choose anouther weapon")
            return False

