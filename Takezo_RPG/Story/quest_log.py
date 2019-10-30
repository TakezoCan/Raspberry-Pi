

class Quest(object):
    quest_name = ""
    quest_desc = ""
    objects = {}

    def __init__(self, name):
        self_name = name
        Quest.objects[self.quest_name] = self

    def get_log(self):
            return "\n" + self.quest_name + ":\n" + self.log + "\n\n" + "-"*90 +"\n\n"

class Little_Bell(Quest): # Little Bell Quest
    def __init__(self,name):
        self.quest_name = "Little Bell" #Quest name
        self.num = 1 # Quest number
        self.log = "" # log
        self.active = False
        super().__init__(name)    
