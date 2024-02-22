# INF 360 - Programming in Python
# Dylan Tomlinson
# Final Project

'''
This is a text adventure game with multiple branches leading to different endings
depending on the player's input. The program uses functions to separate sections of
code. Most of the input sections follow the same structure to sanitize inputs. The
program uses global variables to track some player information that help to determine
different endings.
'''

import logging
logging.basicConfig(filename='FinalProjectLog.txt', level=logging.DEBUG,  # this config writes to a separate file
                    format='%(asctime)s -  %(levelname)s -  %(message)s')   # format for my log
try:
    import DylanTomlinsonFunctions as DTF           # importing all functions and renaming DTF
    logging.debug('DylanTomlinsonFunctions.py loaded successfully')     # logging to debug file if import is successful
except:
    print('DylanTomlinsonFunctions.py is missing! Program will now exit.')      # printing to console if functions file is missing
    logging.critical('DylanTomlinsonFunctions.py is missing! Program will now exit.')       # then logging to debug file
    quit()          # ending the program


# calling the functions in the necessary order
DTF.titleCard()

DTF.branch1()
DTF.middleText()
DTF.branch2()
DTF.enterHome()
DTF.branch3()
DTF.policeAnswered()
DTF.climax()
