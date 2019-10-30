
import random
import time
from utilities import util
from Characters import gameobjects
from Characters import player
from Characters import get_name
from Characters import get_object
from Story import quest_log



def getWeapon():
    player.name = "..."
    player.exp = 0
    player.lvl = 1
                           # Name,       ,exp,             lvl,      ac, strength, intel, weapon 1, att_die
    Tak = player.Character(player.name, player.exp,    player.lvl,   10,    10,     10,   "none",     0 ,   "none", 0)

                             #  Quest Name, 
    LtlBell = quest_log.Little_Bell("Little Bell")
    LtlBell.active = False
     
    pause = 1.5
    pause2 = 1.25
    exp = 0
   

    print("\t\t\t\tBOOK ONE - EARTH\n\n")# Opening Chapter
    time.sleep(3)
    
    def print1():
        line = 0
        while line < 8:
            print(line_dict1[line])
            time.sleep(pause)
            line = line +1            

    line_dict1 = [
    "\n\tSlowly and painfully you open your eyse, you wake up in a daze...",#0
    "\tYour head hurts... You taste copper in your mouth...",#1
    "\tThere is a strong smell of blood in the air...",#2
    "\tYou are having a hard time remembering who you are...",#3
    "\tAnd where you are...\n",#4
    '\n\t"W... What... What is my name?" you ask yourself...',#5
    "\tA name slowly works its way into your mind...",#6
    "\tWas it Takezo?... \n\n\n" +"-"*90 +"\n",#7
    ]


    print1()
    Takezo=util.yesOrNo("Do you want to use the name Takezo? (Y/N) >> ")
    if Takezo:
        player.name = "Takezo"
    else:
        player.name = get_name.getName()
    print("\n\n" +"-"*90 +"\n")


    def print2():
        line = 0
        while line < 14:
            print(line_dict2[line])
            time.sleep(pause2)
            line = line +1

    line_dict2 = [
    "\n\tYou have a horrible headake...",#0
    "\tYour memory is still a little foggy...",#1
    "\tYet you are able to remember that your name is... " + player.name,#2
    "\n\t" + player.name + ", You manage to lift your head a little.",#3
    "\tYou take a look around...",#4
    "\tLow dark clouds float accross the ominous sky...",#5
    "\tThere are dead horses and dead [bodies] everywhere...",#6
    "\tThousands of them...",#7
    "\tYou look down at your[self] and at the [ground]...",#8
    "\tThere is blood everywhere...",#9
    "\tHow long have I been here?...",#10
    '\t"Was I in a battle? How am I still alive?" You ask yourself...\n',#11
    "\tIs the battle still going on?...",#12
    #"\t",
    "\t" + player.name + ", You realise that you need a weapon...\n\n" +"-"*90 +"\n"#13
    ]
    
    print2()
    
    def get_input():
        
        player.att_die1 = 0
        player.weap1 = "none"
        
        command = input("\nWhat do you want to do? [search] [examine] [say]\n\nCommand >> ").split()
        verb_word = command[0]
        
        end = False
               
        if verb_word == "hit":
            verb = verb_word
            print("There is nothing here to hit")
            return False
        elif verb_word in verb_dict1:
            verb = verb_dict1[verb_word]               
        else:
            print("Unknown verb {}" .format(verb_word))
            return False
        
        if len(command) >= 2:
            noun_word = command[1]
            if noun_word == "bodies" and LtlBell.active == True:
                print("\n\t\tYou already searched the bodies.")
            else:
                print (verb(noun_word))            
        else:
            print(verb("nothing"))
        

        if player.att_die1 > 0: # Did the player equip a weapon?
            end = True
        else:
            end = False

        return end
        
        

    def say(noun):
        return '\nYou said "{}".\n'.format(noun) + "-"*90 + "\\n"
    
    def examine(noun):
        if noun == "ground":
            return"""\n\n\tThe ground is covered in bodies, and blood...
\tThere are flies buzzing around everywhere
\tIt looks like there might be something else here...
\tIf you [search] closer....\n\n"""
        elif noun == "bodies":
            return"""\n\n\tThe bodies smell foul and look even worse...\n\n"""
        elif noun == "self":
            return """\n\n\tYour head still hurts and you are covered in blood...\n\n"""
        elif noun == "sky":
            return "\n\n\tNow is not the time for cloud watching...\n\n"
        else:
            return "\n\nThere is no {} here.\n\n\n" + "-"*90 + "\n".format(noun)

    def search(noun):
                         
        if noun == "bodies":
            LtlBell.log = "Battlefield bodies did not have wapons... Currious."
            LtlBell.active = True
            exp =1
            player.lvl = get_object.Level(exp)
            return """\n\n\tThat's strange... There are no weapons here...
\tThese warriors should have weapons!\n\tYou gaind 1 experience point\n\n"""
        
        if noun == "sky":
            return "\n\n\tYou look to the gods for answers and find none...\n\n"
        
        elif noun == "ground":
            
            yes = util.yesOrNo("\n\nYou find a stick on the ground,\nDo you want to use it as a weapon? (Y/N) >> ")
            if yes:
                weapon = get_object.gameWeapon("stick")
                if not weapon:
                    return "\n\n" + "-"*90 + "\n\n"
                else:
                    player.att_die1 = weapon
                    player.weap1 = "stick"
                    exp = 6
                    player.lvl = get_object.Level(exp)
                    return "\n\nI guess this stick will have to do for now.\n\t\tYou gained 6 experience ponts\n\n" + "-"*90 + "\n"
                
            else:
                yes = util.yesOrNo("\nDo you want to use your fists as a weapon? (Y/N) >> ")
                if yes:
                    weapon = get_object.gameWeapon("fist") 
                    if not weapon:
                        return "\n\n" + "-"*90 + "\n\n"
                    else:
                        player.att_die1 = weapon
                        player.weap1 = "fist"
                        exp = 5
                        player.lvl = get_object.level(exp)
                        return "\n\nI guess i'll have to use my fists for now.\n\t\tYou gained 5 experience points\n\n-" + "-"*90 + "\n"
                    
                else:
                    return "\n\n" + "-"*90 + "\n\n"
        else:
            player.att_die = 0
            return '\n\nYou cannot search "{}" \n\n'.format(noun) + "-"*90 + "\n"
            
            
            
    verb_dict1 = {
        "say":say,
        "examine":examine,
        "search":search,
    }

    end = False    
    while end == False:              
        end = get_input()
    else:
        return False
       
        

