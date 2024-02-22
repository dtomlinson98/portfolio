# INF 360 - Programming in Python
# Dylan Tomlinson
# Final Project

import time  # time module used for delaying print function
import random  # random module used to produce lucky number that grants player phone service
import logging  # logging module for logging numerous errors and information
try:
    import DylanTomlinsonPlayer as DTP              # importing player object
    logging.debug('DylanTomlinsonFunctions.py loaded successfully')
except:
    print('DylanTomlinsonPlayer.py is missing! Program will now exit.')      # printing to console if functions file is missing
    logging.critical('DylanTomlinsonPlayer.py is missing! Program will now exit.')       # then logging to debug file
    quit()          # ending the program


logging.basicConfig(filename='FinalProjectLog.txt', level=logging.DEBUG,  # use this config to write to separate file
                    format='%(asctime)s -  %(levelname)s -  %(message)s')  # final project config
battery = ''  # global battery variable to track players phone battery
weapon = bool  # empty weapon variable set to accept a boolean type value


def titleCard():  # function that prints title card and asks user to play or not
    print(''''
                    ]___________ ____ _______[
                   ======== =============== =
                  /WWWWWWWWW WWWWWWWWWWW W    =
               /WW ^ WWWWWWWWWWWW   WW  WWW ^ WW   \ 
             W WW/___\WWWWW WWWWWWWW  WW W/___ WW\                     
          /WWWW/_______\ WWWWWWWWWW  WW /_______\WW   W                                     
       /WW WWWW|   #   | WWWWWWWWWW WWWW|   #   |WWWWW W                            
    /WWWWWWWWWW|_______|WWWWWW W W   WWW|_______|WWW  WWWWW
     ]_____   ___[]____ _______ ]____  ______[]___ _______[]                                                                                    
      ::::::::::::::::::::::::: ::::::::::::::::::::::::
      :::::::::|___|___|::::::   :::::::|___ ___|:::::::::  :      
      :::::::::|_  ____|::: -------- :::|_ _____ ::::::::::
      ::::::::: ___|___|:::|   THE    ::|___|___|::::::::::
      :::::::::::::::::::::|  HOUSE  |:::::::::::::::::::::
      :: :::::::::::::::::   0       |:::::::::::::::  :::: :
      :::::::::::::::::::::|         |:::::::::::::::::::::
    ::::::::::::::  :::::::|______ __|::::::   ::::::::::::::
          ''')
    choices = ['Y', 'N']  # list containing two elements that represent choices
    playGame = ''  # empty variable which will hold the user's input
    while playGame not in choices:  # while loop that repeats an input prompt until the user makes a valid input
        playGame = input('Would you like to play THE HOUSE?(Y/N) '.center(50)).upper().strip()
        if playGame == 'Y':  # if the user says y or Y the introText() funciton will be called
            player = DTP.Player()   # setting Player object to variable player
            player.setName()    # calling setName() method to ask a player for their name
            print('Welcome to THE HOUSE, ' + player.name)   # using player.name to call the name that was set in setName() method
            time.sleep(1)
            player.printBattery()
            player.printWeapon()
            time.sleep(1)
            introText()
            break
        elif playGame == 'N':  # if the user says n or N print the following
            print('Okay, thanks anyways.'.center(50))
            quit()  # quit program


def introText():  # function with print functions for the story
    print('#' * 62)
    print('You just moved into a small town outside of the city.')
    time.sleep(3)  # time module used routinely to delay prints
    print('There isn\'t much nearby, except for one rundown\nhouse across the road.')
    time.sleep(3)
    print('Everyone in town says no one has lived there in years but\nyou\'ve noticed strange '
          'noises every night since you moved in.')
    time.sleep(4)
    print('Nothing serious enough to look into but something about tonight\nfeels different.')
    time.sleep(4)
    print('As the night comes to an end, your eyes begin to get heavier\nand heavier until you hear something...')
    time.sleep(5)
    print('\'AAHHHH!\''.center(50))
    time.sleep(2)


def branch1():
    choices1 = ['investigate', 'stay']  # similar loop structure as before
    decision1 = ''
    while decision1 not in choices1:
        decision1 = input('''
**Investigate the noise or stay home.(investigate/stay)** ''').lower().strip()
        if decision1 == 'investigate':
            print('Your eyes spring open and you run over to the window.')
            break
        elif decision1 == 'stay':
            print('The blood curdling scream sends you into a panic.')
            time.sleep(2)
            print('You lock up your house and go to your bedroom to turn in for the night.')
            time.sleep(3)
            print('When morning comes, you only remember a bad dream...')
            quit()


def middleText():  # function with print functions for the story
    time.sleep(2)
    print('All you can make out is the old rotting roof that is partially illuminated\nby the moon.')
    time.sleep(3)
    print('Everything else is shrouded in a dense fog.')
    time.sleep(2)
    print('\'Someone could be hurt\'-- you think to yourself'.center(50))  # I used .center() to make dialogue stand out more
    time.sleep(3)
    print('You run out to your driveway and across the road.')
    time.sleep(2)
    print('\'AAHHHHHHH! H-Help me!\''.center(50))  # escape characters to print quotes
    time.sleep(3)
    print('As you get closer to the screams, you can tell it is coming from\ninside the house and it is a young boy.')
    time.sleep(3)
    print('You stop to think over your options...')
    time.sleep(2)


def phoneAnswer():  # function that creates a random number
    phoneService = random.randint(1, 10)  # in the next function the player will have a choice to call the police
    logging.debug(f'The random number was: {phoneService}')     # this will log what the random number was to my logging file
    if phoneService == 7:  # if they decide to and their random number is 7, they will connect with the police
        time.sleep(5)
        print('\'Come on. Come on!\''.center(50))  # but their phone battery will go to zero making their phone defective for the rest of the game.
        time.sleep(3)
        print('\'911, please state your emergency\''.center(50))
        time.sleep(2)
        print('\'Hello! Please help I think someone is hurt!\''.center(50))
        time.sleep(3)
        print('\'Ok, calm down. We can send a unit over but it may take some time, what is your add--\'')
        time.sleep(2)
        print('\'AAHHHH! NOOO!\''.center(50))
        time.sleep(1.5)
        print('\'--BATTERY_DEAD--\''.center(50))
        time.sleep(1)
        print('\'Ugh! I seriously need to lay off tik tok.\'')
        time.sleep(2)
        print('Reluctantly, you walk towards the door.')
        global battery  # calling global variable from earlier in the code
        battery = 0  # this phone call leaves the player with zero battery
    else:
        battery = 10  # if they don't get the lucky number they will receive these print functions
        time.sleep(5)
        print()
        print('\'Come on. Come on!\''.center(50))
        time.sleep(3)
        print('\'Damn! No service!\'-- you scoff in frustration'.center(50))
        time.sleep(3)
        print('Against your better judgment, you approach the house.')


def branch2():
    choices2 = ['enter', 'return', 'police']  # local variable given list value with 3 elements
    decision2 = ''
    while decision2 not in choices2:  # if they don't input one of the three choices in the list, the prompt will be asked again
        decision2 = input('''
 **Enter the house and help the boy, call the police, or return home?(enter/police/return)** ''').lower().strip()
        if decision2 == 'enter':
            print()
            print('You step onto the lawn as a cold breeze gusts over you.')
            global battery
            battery = 10
            break
        elif decision2 == 'police':
            print('You pull out your phone and dial...')
            phoneAnswer()
        elif decision2 == 'return':  # returning home causing the game to end, I plan to add more paths to these branches in the final project
            print('In the moment of fear you lose your courage.')
            print('You return home and search Zillow for a new home.')
            time.sleep(3)
            quit()


def enterHome():  # function with print functions for the story
    time.sleep(3)  # time.sleep() to delay print
    print('As you get to the door you see it\'s broken off the hinges and just\nbalancing in place.')
    time.sleep(3)
    print('You carefully slide around it without knocking it over and enter the house.')
    time.sleep(3)
    print('The smell of mold hits you and the air feels heavy on your body.')
    time.sleep(3)
    print('It\'s dark besides some light coming through the windows from the moon.')
    time.sleep(3)
    print('You can\'t see much other than the faint beginnings of a hallway.')
    time.sleep(3)
    print('You pull out your phone to use the flashlight.')
    print()


def branch3():
    global battery  # calling the global variable battery
    if battery > 0:  # if the player has greater than 0 battery life, run the following code
        choices3 = ['use', 'save']  # local variable given list value with 3 elements
        decision3 = ''
        while decision3 not in choices3:  # if they don't input one of the three choices in the list, the prompt will be asked again
            decision3 = input('''You realize you only have 10% battery left. 
            **Use your flashlight or save it for later?(use/save)** ''').lower().strip()

            if decision3 == 'use':
                battery = 5
                print('You turn on your flashlight and look around.')
                time.sleep(3)
                print('You don\'t see anyone or much of anything just an old rotting house.')
                time.sleep(3)
                print('There is some writing on the wall to your left.')
                time.sleep(3)
                print('You can\'t make out what it says but it\'s written in a black sludge.')
                time.sleep(3)
                print('Just along the wall, near the sludge, you see a table and on top\nlies a hatchet.')
                print()
                takeWeapon = input('**Take the hatchet or search the house.(take/search)** ').lower().strip()
                if takeWeapon == 'take':
                    global weapon
                    weapon = True  # tracking that the player does have a weapon
                    print('\'I got a feeling I\'ll need this.\''.center(50))
                elif takeWeapon == 'search':
                    weapon = False  # tracking that the player does not have a weapon
                    battery = 5  # tracking the player's battery life
                    print('You step deeper into the house.')
                else:
                    weapon = False
                    print('You failed to make a decision.')
            elif decision3 == 'save':
                battery = 10  # tracking the player's battery life
                weapon = False
                print('\'UGH! I better save this.\''.center(50))


def policeAnswered():  # this function will only be called if the player's random number
    global battery  # was 7 and the code was run to talk to the police
    global weapon
    if battery == 0:
        weapon = False  # it is a hidden ending most won't get on their first play through
        time.sleep(2)
        print('\'Damn! Out of juice.\''.center(50))
        time.sleep(2)
        print('\'I can\'t see anything in here\''.center(50))
        time.sleep(2)
        print('\'AHH! RUUUN!\''.center(50))
        time.sleep(1)
        print('A large black sludge rolls down the basement and charges towards you.')
        time.sleep(3)
        print('You can\'t make out what it is and as you turn to run it grabs your leg.')
        time.sleep(3)
        print('It moves higher and higher up your body, slowly constricting you.')
        time.sleep(3)
        print('Everything begins to get dark until--')
        time.sleep(1.5)
        print('\'GET OFF OF HIM!\''.center(50))
        time.sleep(2)
        print('The sludge releases you and moves towards the boy.')
        time.sleep(2)
        print('Then the inside of the house is lit with red and blue lights.')
        time.sleep(2)
        print('The sludge retreats out the back of the house and into the woods.')
        time.sleep(3)
        print('As the police enter you look at the boy and try to make sense of what just happened.')
        time.sleep(3)
        print('#####YOU WERE ABLE TO SAVE THE BOY BUT THE DEMON ESCAPED#####'.center(50))
        quit()


def climax():
    if battery > 0:  # runs as long as phone battery is greater than 0
        time.sleep(3)  # this keeps the code from showing to players who received the
        print('\'AAHHHH!\''.center(50))  # the lucky number
        time.sleep(2)
        global weapon
        if weapon == True:  # if they have a weapon run this code
            print('You run upstairs toward the scream and find the little boy held\nagainst the wall.')
            time.sleep(3)
            print('There\'s nothing holding him, just a mass of black sludge engulfing\nhim feet first.')
            time.sleep(3)
            print('As you look on in terror, you reach for the hatchet.')
            time.sleep(2)
            print('\'Ahhh! Die Demon!\''.center(50))
            print('The hatchet does nothing to the entity as it engulfs you along with the boy.')
            time.sleep(3)
            print('#####YOU WERE ILL-EQUIPPED TO FACE THE DEMON#####'.center(50))
            quit()
        elif weapon == False and battery == 5:  # if they have no weapon and batter of 5 run this code
            time.sleep(2)
            print('You start towards the screams but remember--')
            time.sleep(2)
            print('\'The hatchet!\''.center(50))
            print('You run back to the table and search for it but can\'t find it in the darkness.')
            time.sleep(3)
            print('\'AAHHHH! H-HELP\''.center(50))
            time.sleep(1)
            print('You pull out your phone and turn on your flashlight.')
            time.sleep(3)
            print('\'Where is it!\''.center(50))
            time.sleep(1)
            print('--Battery-Dead--')
            print('\'NO!\'')
            time.sleep(.5)
            print('\'AAHHHH!\''.center(50))
            print('With no weapon, you flee the house!')
            print('The next day you read in the paper about a lost little boy.')
            time.sleep(3)
            print('#####YOU CHOSE NOT TO SAVE THE BOY#####'.center(50))
            quit()
        elif battery == 10:  # or if they have a battery of 10
            time.sleep(2)
            print('You look around the room for something to defend yourself with.')
            time.sleep(3)
            print('You can\'t see anything in the dark.')
            time.sleep(2)
            print('Then you remember your phone and use the flashlight.')
            time.sleep(2)
            print('With just enough battery left, you search the kitchen and find a fire\nextinguisher.')
            time.sleep(2)
            print('\'This will have to do!\''.center(50))
            time.sleep(2)
            print('You run up the stairs and find a bubbling entity of black sludge.')
            time.sleep(2)
            print()
            print('\'What are you!?!?\''.center(50))
            time.sleep(2)
            print('You see the boy is being strangled as the sludge engulfs him')
            time.sleep(3)
            print('You point and aim the fire extinguisher at the sludge and let him have it.')
            time.sleep(3)
            print(
                'The creature slowly releases the boy and you both look at one another\nin a much needed moment of relief.')
            time.sleep(3)
            print('#####YOU DEFEATED THE DEMON#####'.center(50))
            quit()
