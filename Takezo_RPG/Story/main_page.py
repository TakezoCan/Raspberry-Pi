
import time
from utilities import util


def startScreen():
 
    def get_input():
        print("""\n\t\t\t\t  THE ADVENTURES OF
\t\t\t\t\tTAKEZO!

\t\t\t Based on Eiji Yoshikawa's "Musashi"\n\n\n""")
        
        
        yes = util.yesOrNo("Do you want to start the adventure? (Y/N) >> ")
        print("\n\n"+ "="*90 + "\n\n")
        time.sleep(0.5)
        if yes:
            return True
        else:
            return False
                         
    start = get_input()
    
    if start == True:    
        return True
    else:
        return False
       
        

