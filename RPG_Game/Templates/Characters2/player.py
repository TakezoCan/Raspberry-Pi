from Characters2 import gameobjects      

class Character(gameobjects.GameObject):

    def __init__(self,name, lvl, ac, strength, att_die):
        self.name = name
        self.class_name = "player"
        self.lvl = lvl
        self.ac = ac
        self.strength = strength
        self.att_die = att_die
        self.start_hp = int(lvl/lvl+10)
        self.health = int(lvl/lvl+10) # Running total of player's hit points
        self._desc = "You have %i hit points." % (self.health)
        self.dead = False
        super().__init__(name)

    @property
    def desc(self):
        if self.health > 0:
            return "You have %i hit points." % (self.health)
        else:
            return "You have 0 hit points.\nYou are dead!"

    @desc.setter
    def desc(self,value):
        self._desc = Value

