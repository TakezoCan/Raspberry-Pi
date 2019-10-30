
import random
import time
from utilities import util
from Characters import player
from Story import main_page
from Story import intro
from Story import battle1
from Story import battle2

# Main Game loop
def GameLoop():
    start=main_page.startScreen()
    if start:
        intro.getWeapon()
        
        win = battle1.BattleLoop()
    
        if win == True:
            win = battle2.BattleLoop()
            if win == True:
                pass
        print("\n\t\t\t\tGAME OVER\n\n"+ "="*90 + "\n\n")
        return True
    else:
        print("\n\t\t\t\tGoodbye\n\n")
        return False
    
   
try:
    cont = True
    while cont == True:
        cont = GameLoop()   
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print ("\n\t\t\t\tGoodbye\n\n")


