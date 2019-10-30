
import random
import time
from Characters2 import gameobjects
from Characters2 import player
from Characters2 import goblin
from Characters2 import orc




def BattleLoop():

                       # Name,   lvl, ac, strength, att_die
    Tak = player.Character("Takezo",  5,   1,    1,       8)
     
                      #    Name      lvl, health, ac, strength, att_die
    goblin1 = goblin.Goblin("The gobblin",  1,     4,    0,    0,        4)
    
             # Name      lvl, health, ac, strength, att_die
    orc1 = orc.Orc("The orc",  1,     8,    0,    2,        6)

    
    def get_input():
              
        command = input("\nWhat do you want to do?\n[hit] [examine] [say] [run]\n\nCommand >> ").split()
        verb_word = command[0]
        run = False
        if verb_word == "run": # Exit game and run away
            print("\n\t\tYou run away!\n")
            run = True
            return run
        elif verb_word in verb_dict:
            verb = verb_dict[verb_word]
        else:
            print("Unknown verb {}" .format(verb_word))
            return
        
        if len(command) >= 2:
            noun_word = command[1]
            print (verb(noun_word))
        else:
            print(verb("nothing"))
        return run

    def say(noun):
        return 'you said "{}"'.format(noun)
    
    def examine(noun):
        if noun in gameobjects.GameObject.objects:
            return gameobjects.GameObject.objects[noun].get_desc()
        else:
            return "\nThere is no {} here.\n\n-------------------------------------------------\n".format(noun)

    def hit(noun):
        
        if noun in gameobjects.GameObject.objects:
            thing = gameobjects.GameObject.objects[noun]

            def win(char1, char2):
                
                if(char1.health > char2.health):
                      winner = char1.name
                else:
                    winner = char2.name
                print("%s has won!!\n" % winner)
                
                
            def fight(Char1, Char2):
                
                y = 0
                z = 0 
                    
                z = Char2.damage(Char1.attack()) # Player attack
                time.sleep(0.5)

                if z != 1:
                    y = Char1.damage(Char2.attack()) # Enemy attack
                    time.sleep(0.5)
                                
                if y == 1 or z == 1:
                    win(Char1,Char2)                   
                
            if Tak == thing:
                msg = "\nLife is too short to end it this early!\nCannot attack yourself\n\n-------------------------------------------------"

            elif Tak.health > 0 and thing.health > 0:
                msg = "\n-------------------------------------------------"
                fight(Tak,thing) # Start fight sequence
            elif thing.health <= 0:
                msg = run = "\n%s is dead!\n\n-------------------------------------------------" % (thing.name)
            else:
                msg = "%s dead!\n\n-------------------------------------------------"% (Tak.name)
                
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
        
        
        

