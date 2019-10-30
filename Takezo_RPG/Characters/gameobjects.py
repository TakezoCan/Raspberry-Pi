import random

class GameObject(object): # Main Class
        class_name = ""
        desc = ""
        objects = {}

        def __init__(self,name):
            self.name = name
            GameObject.objects[self.class_name]=self

        def get_desc(self):
            return "\n" + self.class_name + ":\n" + self.desc + "\n\n" + "-"*90 +"\n\n"

        def block (self): # Ability to block
                num = int(self.ac/4) 
                randInt = random.randint(0, num) 
                return randInt/2
                
        def damage(self,dmg): # Amount of damage recieved

            block = self.block()

            if dmg-block < 0:
                dmg = 0
                
            else:
                dmg = dmg-block
            
            self.health -= dmg
                       
            if (self.health <= 0):
                print("%s has lost %i health!" % (self.name, dmg))
                print("%s has died!\n" % self.name)
                self.dead = True
                return 1
            else:
                print("%s has lost %i health!" % (self.name, dmg))
                return 0

        def attack(self): # Ability to attack
            dmg = 0
            randint = random.randint(1,20) + (self.intel/2)
            if randint > 10:
                die_role = random.randint(1,self.att_die1)
                dmg = int(self.strength/4) + die_role
                print ("\n%s's Attack Successful!" % self.name)
            
            else:
                print ("\n%s missed!" % self.name)
            return dmg 

        

