# INF 360 - Programming in Python
# Dylan Tomlinson
# Final Project

class Player:
    species = 'Human'            # use this variable as an overall identifier
    name = ''
    def __init__(self):
        self.name
        self.battery = 10
        self.weapon = False

    def setName(self):
        while True:         # getting a players name
            name = input('**What is your name?** '.center(50))
            if not name.istitle():
                print('That is not a valid. You must capitalize it.')
            else:
                self.name = name
                break

    def printName(self):
        print(str(self.name))

    def printBattery(self):
        print('Phone Battery: ' + str(self.battery))

    def printWeapon(self):
        if self.weapon == False:
            print('Weapon: NONE')
        else:
            print('Weapon: Hatchet')
