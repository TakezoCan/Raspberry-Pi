
import random
import time
from utilities import util
from Characters import get_name
from Characters import weapons
from Characters import player
from Story import battle1
from Story import battle2


def GameLoop():
    player.name = get_name.getName()
    weapon = weapons.getWeapon()
    player.att_die = weapon
    win = battle1.BattleLoop()
    if win == True:
        win = battle2.BattleLoop()
        if win == True:
            pass
    print("\n\t\tGAME OVER\n")
    
   
try:
    GameLoop()   
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print ("\t\tGoodbye\n")


