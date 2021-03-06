from Characters import gameobjects

class Dog(gameobjects.GameObject): # Goblin Character
    def __init__(self,name, lvl ,hp, ac, strength, intel, att_die1):
        self.class_name = "dog" #Enemy class name
        self.lvl = lvl # Level of enemy
        self.start_hp = hp #Enemy's starting hit points
        self.health = hp #Running total of enemy's hit points
        self.ac = ac
        self.strength = strength
        self.intel = intel
        self.att_die1 = att_die1
        self._desc = "Rabid dog, foaming at the mouth" # Dexcription of enemy
        self.dead = False
        super().__init__(name)      

                    
                    
    @property # Dexcription of enemy dependant on health
    def desc(self):
        if self.health >= self.start_hp:
            return self._desc
        elif self.health > (self.start_hp * 0.75) and self.health != self.start_hp:
            health_line = "It has a small wound.\n"
        elif self.health < (self.start_hp * 0.75) and self.health >= (self.start_hp * 0.5):
            health_line = "It has a deep cut on it's back.\n"
        elif self.health < (self.start_hp * 0.5) and self.health >= (self.start_hp * 0.25):
            health_line = "It's leg has been cut off!\n"
        elif self.health < (self.start_hp * 0.25) and self.health > 0:
            health_line = "It is close to death"
        elif self.health <= 0:
            health_line = "It is dead.\n"
        return self._desc + ":\n" + health_line

    @desc.setter # Description of enemy
    def desc(self,value):
        self._desc = Value
