
try:
    
    def get_input():
        command = input("What? :").split()
        verb_word = command[0]
        if verb_word in verb_dict:
            verb = verb_dict[verb_word]
        else:
            print("Unknown verb {}" .format(verb_word))
            return
        if len(command) >= 2:
            noun_word = command[1]
            print (verb(noun_word))
        else:
            print(verb("nothing"))

    def say(noun):
        return 'you said "{}"'.format(noun)
    
    class GameObject(object):
        class_name = ""
        desc = ""
        objects ={}

        def __init__(self,name):
            self.name=name
            GameObject.objects[self.class_name]=self

        def get_desc(self):
            return "\n" + self.class_name + "\n" + self.desc + "\n"

    class Goblin(GameObject):
        def __init__(self,name):
            self.class_name = "goblin"
            self.health = 3
            self._desc = "A foul creature"
            super().__init__(name)
            
        @property
        def desc(self):
            if self.health>=3:
                return self._desc
            elif self.health == 2:
                health_line = "It has a wound on its knee.\n"
            elif self.health == 1:
                health_line = "It's arm has been cut off!\n"
            elif self.health == 0:
                health_line = "It is dead.\n"
            return self._desc + "\n" + health_line

        @desc.setter
        def desc(self,value):
            self._desc = Value
            
    goblin = Goblin("Gobbly")

    def examine(noun):
        if noun in GameObject.objects:
            return GameObject.objects[noun].get_desc()
        else:
            return "\nThere is no {} here.\n".format(noun)

    def hit(noun):
        if noun in GameObject.objects:
            thing = GameObject.objects[noun]
            if type(thing) == Goblin:
                thing.health = thing.health - 1
                if thing.health <= 0:
                    msg = "\nYou killed the goblin!\n"
                else:
                    msg = "\nYou hit the {}\n".format(thing.class_name)
        else:
            msg ="\nThere is no {} here\n".format(noun)
        return msg

        
    verb_dict = {
        "say":say,
        "examine":examine,
        "hit":hit,
    }

    while True:
        get_input()
        
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print ("\t\tGoodbye\n")
