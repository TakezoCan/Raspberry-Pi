
import random
import time
import battle


def GameLoop():
    battle.BattleLoop()
    print("\n\t\tGAME OVER\n")
    
   
try:
    GameLoop()   
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print ("\t\tGoodbye\n")


