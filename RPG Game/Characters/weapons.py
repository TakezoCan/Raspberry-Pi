from utilities import util        
    
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
        affirm = util.yesOrNo("Is this correct? >> ")
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
    
paddle = Paddle("paddle", 1000, 1000000)
            
"""          
fist = weapon("fist", 2, 0)
kubaton = weapon("kubaton", 4, 5)         
knife = weapon("knife", 4, 5)
stick = weapon("stick", 4, 0)
rusty_sword = weapon("rusty-sword", 6, 10)
short_sword = weapon("short-sword", 7, 50)
sword = weapon("sword", 8, 100)
tanto = weapon("tanto", 10, 300)
katana = weapon("katana", 15, 500)
staff = weapon("staff",  10, 150)
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
           

weapon_list = {
    "fist",
    "kubaton",         
    "knife",
    "stick",
    "rusty_sword",
    "short_sword",
    "sword",
    "tanto",
    "katana",
    "staff",
    "paddle"
 }

