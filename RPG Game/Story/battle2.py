
import random
import time
from utilities import util
from Characters import gameobjects
from Characters import player
from Characters import goblin
from Characters import orc




def BattleLoop():

                           # Name,   lvl,  ac, strength, intel, att_die
    Tak = player.Character(player.name,  5,   15,    16,     10,      player.att_die)
     
                           #    Name      lvl, health, ac, strength, intel, att_die
    goblin1 = goblin.Goblin("The gobblin",  1,     4,    4,    4,      2,      4)
    
                  # Name      lvl, health, ac, strength, intel, att_die
    orc1 = orc.Orc("The orc",  1,     8,    6,    6,       4,      6)


    print("\n\t\t" + player.name + ", You enter the forest when a foul smelling\n\t\tgoblin and an ugly orc jump out at you!\n\n """)

    
    def get_input():
        
              
        command = input("\nWhat do you want to do? [hit] [examine] [run] [say]\n\nCommand >> ").split()
        verb_word = command[0]
        
        run = False
        if verb_word == "run": # Exit game and run away
            run = util.yesOrNo("\nYou want to " + verb_word + ".\nAre you sure? (Y/N) >> ")
            if run == True:
                print("\n\t\tYou run away!\n")
                return True
            else:
                return False
            
        elif verb_word in verb_dict:
            verb = verb_dict[verb_word]
        else:
            print("Unknown verb {}" .format(verb_word))
            return False
        
        if len(command) >= 2:
            noun_word = command[1]
            print (verb(noun_word))
        else:
            print(verb("nothing"))
        if goblin1.health <= 0 and orc1.health <=0:
            run = True
            print("\n\t\tYou win the battle!")
            return run
        elif Tak.health <= 0:
            run = True
            print("You lost the battle!")
            return run      
        return run

    def say(noun):
        return '''\nYou said "{}" and the creatures grunt in return.\n
-------------------------------------------------\n'''.format(noun)
    
    def examine(noun):
        if noun in gameobjects.GameObject.objects:
            return gameobjects.GameObject.objects[noun].get_desc()
        else:
            return "\nThere is no {} here.\n\n-------------------------------------------------\n".format(noun)
    def go(thing1, thing2):
        
        def win(char1, char2, char3):
                
            if char1.health > char2.health:
                winner = char1.name
                not_winner = char2.name
            elif char1.health > char3.health:
                winner = char1.name
                not_winner = char3.name
            else:
                winner = char2.name +" and "+ char3.name
                not_winner = char1.name
            print("%s has killed" % winner)
            print("%s!" % not_winner)
                
        def fight(Char1, Char2, Char3):
            x = 0
            y = 0
            z = 0 
                    
            z = Char2.damage(Char1.attack()) # Player attack
            time.sleep(0.5)

            if Char2.health > 0:
                x = Char1.damage(Char2.attack()) # First Enemy attack
                time.sleep(0.5)
                        
            if Char3.health > 0:
                z = Char1.damage(Char3.attack()) # Second Enemy attack
                time.sleep(0.5)
                                
            if x == 1 or y == 1 or z == 1:
                     win(Char1,Char2,Char3)
            
        if Tak == thing1:
            msg = "\nLife is too short to end it this early!\nCannot attack yourself\n\n-------------------------------------------------"

        elif Tak.health > 0 and (thing1.health > 0 or thing2.health > 0):
            msg = "\n-------------------------------------------------"
            fight(Tak,thing1,thing2) # Start fight sequence
                
        elif thing1.health <= 0 and thing2.health <= 0:
            msg = "The enemy's are dead!\n\n-------------------------------------------------"
            
        else:
            msg = "%s dead!\n\n-------------------------------------------------"% (Tak.name)
        return msg
                          


    def hit(noun):
        if noun in gameobjects.GameObject.objects and noun == "goblin":
            thing1 = gameobjects.GameObject.objects[noun]
            thing2 = gameobjects.GameObject.objects["orc"]
            msg = go(thing1, thing2)
            
        elif noun in gameobjects.GameObject.objects and noun == "orc":
            thing1 = gameobjects.GameObject.objects[noun]
            thing2 = gameobjects.GameObject.objects["goblin"]
            msg = go(thing1, thing2)         

            
        else:
            msg ="\nThere is no {} here\n\n-------------------------------------------------".format(noun)
        return msg    

        
    verb_dict = {
        "say":say,
        "examine":examine,
        "hit":hit,
    }

    end = False    
    while end == False:              
        end = get_input()
    if Tak.health > 0 and goblin1.health < 0 and orc1.health < 0:
        return True
    else:
        return False
        
        
        

