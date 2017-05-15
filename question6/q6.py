import numpy as np

class ship:
    
    # Constructor
    def __init__(self, names):
        self.shields=100
        self.hull=100
        self.alive=True
        self.name=names
        
    def shoot(self, target):
        if self.alive==True:
            strength=10
            target.takehit(strength)

    def takehit(self, strength):
        if self.shields > 0:
            self.shields=self.shields-strength
        else:
            self.hull = self.hull -strength
        if self.hull<=0:
            self.alive=False
            print self.name+" was destroyed!"
        print self.name+" took a hit for "+str(strength)+" damage!"

    def __str__(self):
        return 'Ship Name: ' + self.name +'\n' 'Remaining shields: ' + str(self.shields) +'\n'+'Remaining hull strength: ' + str(self.hull) +'\n'

class warship(ship):
    
    def shoot(self, target):
        if self.alive==True:
            if np.random.random(1) > 0.7:
                strength=30
            else:
                strength=10
            
            target.takehit(strength)



class speeder(ship):
    def __init__(self, names):
        ship.__init__(self, names)
        self.hull=50
    def takehit(self, strength):
        if np.random.random(1) > 0.3:
            print self.name+" took a hit for "+str(strength)+" damage!"
            if self.shields > 0:
                self.shields=self.shields-strength
            else:
                self.hull = self.hull -strength
            if self.hull<=0:
                self.alive=False
                print self.name+" was destroyed!"
        else:
            print self.name+" dodged an attack!"



class battle:
    
    # Constructor
    def __init__(self, ship):
        self.ships=ship      
        self.combat=True

    def stepForward(self):
        if self.combat==True:

            np.random.shuffle(self.ships)

            for ship in self.ships:

                for i in range(50):
                    target = self.ships[np.random.random_integers(0,len(self.ships)-1)] 
                    if target.alive == True and target!=ship:
                        break
                ship.shoot(target)
            numalive=0
            for ship in self.ships:
                if ship.alive==True:
                    numalive+=1
            if numalive<=1:
                self.combat=False
        return

    def declareWinner(self):
        iswinner=False
        for ship in ships:
            if ship.alive==True:
                winner=ship
                iswinner=True
        if iswinner==True:
            print '\n'
            print "Battle over - winner has been declared!"
            print winner
            print '\n'
        else:
            print '\n'
            print "No winner -- All ships destroyed!"
            print '\n'








ships=[]
ships.append(ship('Enterprise'))
ships.append(warship('Hyperion'))
ships.append(ship('Millenium Falcon'))
ships.append(speeder('Speeder 17'))
ships.append(ship('Titanic'))



spacebattle=battle(ships)
for ship in spacebattle.ships:
    print ship.name
while spacebattle.combat==True:
    spacebattle.stepForward()

spacebattle.declareWinner()






