from Characters import gameobjects



class Character(gameobjects.GameObject):
                
    def __init__(self,name, exp, lvl, ac, strength, intel, weap1, att_die1, weap2, att_die2):
        self.name = name
        self.class_name = "self"
        self.exp = exp
        self.lvl = lvl
        self.ac = ac
        self.strength = strength
        self.intel = intel
        self.weap1 = weap1
        self.att_die1 = att_die1
        self.weap2 = weap2
        self.att_die2 = att_die2
        self.start_hp = int(lvl/2*1.75)+10
        self.health = int(lvl/2*1.75)+10 # Running total of player's hit points
        self._desc = "You are level %i, with %i hit points.\nYou have a %s for a weapon" % (self.lvl, self.health, self.weap1) 
        self.dead = False
        super().__init__(name)

    @property
    def desc(self):
        if self.health > 0:
            return "You are level %i, with %i hit points.\nYou have a %s for a weapon" % (self.lvl, self.health, self.weap1) 
        else:
            return "You have 0 hit points.\nYou are dead!"

    @desc.setter
    def desc(self,value):
        self._desc = Value

    

    
        
