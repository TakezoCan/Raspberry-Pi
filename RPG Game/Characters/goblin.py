from Characters import gameobjects

class Goblin(gameobjects.GameObject): # Goblin Character
    def __init__(self,name, lvl ,hp, ac, strength, intel, att_die):
        self.class_name = "goblin" #Enemy class name
        self.lvl = lvl # Level of enemy
        self.start_hp = hp #Enemy's starting hit points
        self.health = hp #Running total of enemy's hit points
        self.ac = ac
        self.strength = strength
        self.intel = intel
        self.att_die = att_die
        self._desc = "A foul creature" # Dexcription of enemy
        self.dead = False
        super().__init__(name)      

                    
                    
    @property # Dexcription of enemy dependant on health
    def desc(self):
        if self.health >= self.start_hp:
            return self._desc
        elif self.health > (self.start_hp * 0.75) and self.health != self.start_hp:
            health_line = "It has a small wound.\n"
        elif self.health < (self.start_hp * 0.75) and self.health >= (self.start_hp * 0.5):
            health_line = "It has a wound on its knee.\n"
        elif self.health < (self.start_hp * 0.5) and self.health >= (self.start_hp * 0.25):
            health_line = "It's arm has been cut off!\n"
        elif self.health < (self.start_hp * 0.25) and self.health > 0:
            health_line = "It is close to death"
        elif self.health <= 0:
            health_line = "It is dead.\n"
        return self._desc + ":\n" + health_line

    @desc.setter # Description of enemy
    def desc(self,value):
        self._desc = Value
