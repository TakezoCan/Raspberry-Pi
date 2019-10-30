
import random
import time
from utilities import util
from Characters import gameobjects
from Characters import player


def BattleLoop():

                           # Name,        exp,          lvl,     ac, strength, intel, att_die
    Tak = player.Character(player.name, player.exp, player.lvl,   5,    10,     8,      player.weap1, player.att_die1, "none", 0)
     
    def print1():
        line = 0
        while line < 8:
            print(line_dict1[line])
            time.sleep(pause)
            line = line +1            

    line_dict1 = [
    "\n\t" + player.name + ", as you look around searching through the bodies,",#0
    "\You remember... you were with someone... a friend... "),#1
    "\tMatusashi!! You start to fanticaly search for your friend",#2
    "\tYou barely get started looking for Matusashi when you hear an animal growl...",#3
    "\tYou Turn and look... staringyou strait in the eyse is an angry dog who is foaming at the mouth...",#4
    "\n\n" +"-"*90 + "\n\n",#7
    ]


    print1()          
    
    
    def get_input():
        
              
        command = input("\nWhat do you want to do? [hit] [examine] [run] [say]\n\nCommand >> ").split()
        verb_word = command[0]
        
                    
        if verb_word in verb_dict:
            verb = verb_dict[verb_word]
        else:
            print("Unknown verb {}" .format(verb_word))
            return False
        
        if len(command) >= 2:
            noun_word = command[1]
            print (verb(noun_word))
        else:
            print(verb("nothing"))
            
                
        

    def say(noun):
        return '\nYou said "{}" and the creature growls in return.'.format(noun) + "\n\n" + "-"*90 + "\n\n"
    
    def examine(noun):
        if noun in gameobjects.GameObject.objects:
            return gameobjects.GameObject.objects[noun].get_desc()
        else:
            return "\nThere is no {} here.\n\n" + "-"*90 + "\n\n".format(noun)

           
    verb_dict = {
        "say":say,
        "examine":examine,
        "hit":hit,
    }

      
    while True:              
        get_input()
    
       
        

