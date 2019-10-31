
import random
import time
from utilities import util
from Characters import gameobjects
from Characters import player
from Characters import get_object
from Characters import dog





def BattleLoop():

                           # Name,        exp,          lvl,     ac, strength, intel, att_die
    Tak = player.Character(player.name, player.exp, player.lvl,   5,    10,     8,      player.weap1, player.att_die1, "none", 0)
     
                 #    Name          lvl, health, ac, strength, intel, att_die
    dog1 = dog.Dog("The rabid dog",  1,     4,    1,    2,       2,      4)
  

    print("\n\t\t" + player.name + ", you enter a swamp when a rabid\n\t\tdog jumps out at you!\n\n ")
    print("\n\n" +"-"*90 + "\n\n")
    
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
            
        if dog1.health <= 0:
            run = True
            print("\n\t\t\tYou win the battle!")
            print("\t\tYou have gained 5 experience ponts")
            exp = 5
            player.lvl = get_object.Level(exp)
            print("\n\n" + "-"*90 + "\n")
            return run
        elif Tak.health <= 0:
            run = True
            print("You lost the battle!")
            return run
        
        return run

    def say(noun):
        return '\nYou said "{}" and the creature growls in return.'.format(noun) + "\n\n" + "-"*90 + "\n\n"
    
    def examine(noun):
        if noun in gameobjects.GameObject.objects:
            return gameobjects.GameObject.objects[noun].get_desc()
        else:
            return "\nThere is no {} here.\n\n" + "-"*90 + "\n\n".format(noun)

    def hit(noun):
        
        if noun in gameobjects.GameObject.objects:
            thing = gameobjects.GameObject.objects[noun]

            def win(char1, char2):
                
                if(char1.health > char2.health):
                    winner = char1.name
                    not_winner = char2.name
                    
                else:
                    winner = char2.name
                    not_winner = char1.name
                print("%s has killed" % winner)
                print("%s!" % not_winner)
                
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
                msg = "\n\n" + "-"*90 + "\n\n"
                fight(Tak,thing) # Start fight sequence
            elif thing.health <= 0:
                msg = run = "\n%s is dead!\n\n"% (thing.name) + "-"*90 + "\n\n" 
            else:
                msg = "%s dead!\n\n"(Tak.name) + "-"*90 + "\n\n"
                
        else:
            msg ="\nThere is no {} here\n\n".format(noun) + "-"*90 + "\n\n"
        return msg 
        
    verb_dict = {
        "say":say,
        "examine":examine,
        "hit":hit,
    }

    end = False    
    while end == False:              
        end = get_input()
    if Tak.health > 0 and dog1.health <= 0:
        return True
    else:
        return False
       
        

