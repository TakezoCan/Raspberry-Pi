
from utilities import util        

def weapInput(prompt):
    weapon = input(prompt)
    return weapon.strip()


def getWeapon():
    
    class weapon(object):
        weapon_name = ""
        objects = {}

        def __init__(self, name, att_die, cost):
            self.name = name
            self.att_die = att_die,
            self.cost = cost
            weapon.objects[self.name] = self
        
    fist = weapon("fist", 2, 0),
    kubaton = weapon("kubaton", 4, 5),         
    knife = weapon("knife", 4, 5),
    stick = weapon("stick", 4, 0),
    rusty_sword = weapon("rusty-sword", 6, 10),
    short_sword = weapon("short-sword", 7, 50),
    sword = weapon("sword", 8, 100),
    tanto = weapon("tanto", 10, 300),
    katana = weapon("katana", 15, 500),
    staff = weapon("staff",  10, 150)
             
    tempWeap = "" 
                
    while True:
        tempWeap = weapInput("\nChoose your weapon. >> ")

                               
        if tempWeap in weapon_list:
            yes = util.yesOrNo(tempWeap + ", is this the weapon you want? (Y/N) >> ")

            if yes:
                charWeap = weapon.objects[tempWeap]
                return charWeap.att_die
            else:
                pass
        else:
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
    "staff"
 }

