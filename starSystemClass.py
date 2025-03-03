#!Python 3

import random

starportLookUpTable = {"A":"Excellent quality starport with refined fuel, overhaul, shipyards.","B":"Good quality starport with refined fuel, overhaul, shipyards for non-starships.","C":"Routine quality starport with unrefined fuel, some repair facilities.","D":"Poor quality starport with unrefined fuel; no repair facilities.","E":"Starport is a frontier installation; no facilities.","X":"No starport."}

mainWorldSizeLookUpTable = {0:"Asteriod/Planetiod Belt",1:"1,000 miles(1 600 km)",2:"2,000 miles(3 200 km)",3:"3,000 miles(4 800 km)",4:"4,000 miles(6 400 km)",5:"5,000 miles(8 000 km)",6:"6,000 miles(9 600 km)",7:"7,000 miles(11 200 km)",8:"8,000 miles(12 800 km)",9:"9,000 miles(14 400 km)",10:"10,000 miles(16 000 km)"}

mainWorldAtmosphereLookUpTable = {0:"No atmosphere.",1:"Trace.",2:"Very thin, tainted.",3:"Very thin.",4:"Thin, tainted.",5:"Thin.",6:"Standered.",7:"Standered, tainted.",8:"Dense.",9:"Dense, Tainted.",10:"Exotic.",11:"Corrosive.",12:"Insidious.",13:"Dense, high.",14:"Ellipsoid",15:"Thin, low."}

mainWorldHydrographicsLookUpTable = {0:"No free standing water.",1:"10% water.",2:"20% water.",3:"30% water.",4:"40% water.",5:"50% water.",6:"60% water.",7:"70% water.",8:"80% water.",9:"90% water.",10:"No land masses."}

populationLookUpTable = {0:"No inhabitans.",1:"Tens of inhabitans.",2:"Hundreds of inhabitans.",3:"Thousands of inhabitans.",4:"Tens of thousands.",5:"Hundreds of thousands.",6:"Millions of inhabitans.",7:"Tens of millions.",8:"Hundreds of millions.",9:"Billions of inhabitans.",10:"Tens of billions."}

govermentLookUpTable = {0:"No goverment struture.",1:"Company/Corparation.",2:"Participating Democracy.",3:"Self-Perpatuating Oligarchy.",4:"Representative Democracy.",5:"Feudal Technocracy.",6:"Captive Goverment.",7:"Balkanization.",8:"Civil Service Bureaucracy.",9:"Impersonal Bureaucracy.",10:"Charismatic Dictator.",11:"Non-Charismatic Leader.",12:"Charismatic Oligarchy.",13:"Religious Dictatorship."}

def lawLevelLookUpTable(lawLevel): 
        if lawLevel <= 0:
            return "No prohibitions. "
        result = ""
        if lawLevel >= 1:
            result += "Body pistols undetectable by standard detectors, explosives, and poison gas prohibited. "
        if lawLevel >= 2:
            result += "Portable ebergy weapons prohibited. "
        if lawLevel >= 3:
            result += "Weapons of a strict military nature prohibited. "
        if lawLevel >= 4:
            result += "Light assault weapons prohibited. "
        if lawLevel >= 5:
            result += "Personal concealable firearms prohibited. "
        if lawLevel >= 6:
            result += "Most firearms prohibited. The carrying of any type of weapon is discouraged. "
        if lawLevel >= 7:
            result += "Shotguns are prohibited. "
        if lawLevel >= 8:
            result += "Long bladed weapons are controlled, and open possession is prohibited. "
        if lawLevel >= 9:
            result += "Possesion of any weapon outside one's residance is prohibited. "
        if lawLevel >= 10:
            result += "Possession of any weapon is prohibited. "
        return result

TechnologicalLevelLookUpTable = {0:"Stone Age or Primitive.",1:"Bronze Age to Middle Ages.",2:"Circa 1400 to 1700.",3:"Circa 1700 to 1860.",4:"Circa 1860 to 1900.",5:"Circa 1900 to 1939.",6:"Circa 1940 to 1969.",7:"Circa 1970 to 1979.",8:"Circa 1980 to 1989.",9:"Circa 1990 to 2000.",10:"Interstellar community.",11:"Average Imperial.",12:"Average Imperial.",13:"Above average Imperial",14:"Above average Imperial",15:"Technical maximum Imperial",16:"Occasional non-Imperial"}

def clamp(n, minimum, maximum):
    if n < minimum:
        return minimum
    elif n > maximum:
        return maximum
    else:
        return n
    
class StarSystem():
    #defalt values for star system
    name = ""
    starport = "X"
    navelBase = False
    scoutBase = False
    gasGiant = False
    mainWorldSize = 0
    mainWorldAtmosphere = 0
    mainWorldHydrographics = 0
    population = 0
    goverment = 0
    lawLevel = 0
    TechnologicalLevel = 0

    def rollDice(self, mod=0, numOfDice=2):
        #mod is what is added to dice roll, defalt 0
        #numOfDice is how many dice are rolled, defalt 2
        roll = mod
        for i in range(numOfDice):
            roll += random.randint(1,6)
        return roll

    def __str__(self):
        #when printed it will return all the stats of the star system based off of the tables descriptions
        if self.navelBase:
            waterbase = "Has a Navel Base."
        else:
            waterbase = "No Navel Base."
        if self.gasGiant:
            gas = "Star system has gas giants."
        else:
            gas = "Star system has only terrestrial planets."
        return f"Star system {self.name}. Starport: {starportLookUpTable[self.starport]} {waterbase} {gas} Main world size: {mainWorldSizeLookUpTable[clamp(self.mainWorldSize,0,10)]} Main world atmosphere: {mainWorldAtmosphereLookUpTable[clamp(self.mainWorldAtmosphere,0,15)]} Main world Hydrograhics: {mainWorldHydrographicsLookUpTable[clamp(self.mainWorldHydrographics,0,10)]} Population: {populationLookUpTable[clamp(self.population,0,10)]} Goverment: {govermentLookUpTable[clamp(self.goverment,0,13)]} Laws: {lawLevelLookUpTable(self.lawLevel)}Technological level: {TechnologicalLevelLookUpTable[clamp(self.TechnologicalLevel,0,16)]}"

    def __init__(self):
        #name generator
        spaceNameTable = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
        for i in range(random.randint(5,8)):
            self.name += spaceNameTable[random.randint(0,36)]
        self.name = self.name.strip()
        #star port generator
        starPorts = ['A','A','A','B','B','C','C','D','E','E','X']
        self.starport = starPorts[self.rollDice(-2)]
        #Navel base generator
        if self.starport != 'C' and self.starport != 'D' and self.starport != 'E' and self.starport != 'X':
            if self.rollDice() >= 8:
                self.navelBase = True
        #Scout base generator
        dm = 0
        if self.starport == 'A':
            dm = -3
        elif self.starport == 'B':
            dm = -2
        elif self.starport == 'C':
            dm = -1
        if self.starport != 'E' or self.starport != 'X':
            if self.rollDice(mod=dm) >= 7:
                self.scoutBase = True
        #Gas giant generator
        if self.rollDice() <= 9:
            self.gasGiant = True
        #Size generator
        self.mainWorldSize = self.rollDice(mod=-2)
        #Atmosphere generator
        if self.mainWorldSize == 0:
            self.mainWorldAtmosphere = 0
        else:
            self.mainWorldAtmosphere = self.rollDice(mod=(self.mainWorldSize-7))
        #Hydrographics generator
        dm = 0
        if self.mainWorldAtmosphere >= 10 or self.mainWorldAtmosphere <= 1:
            dm = self.mainWorldSize - 11
        else:
            dm = self.mainWorldSize - 7
        if self.mainWorldSize <= 1:
            self.mainWorldHydrographics = 0
        else:
            self.mainWorldHydrographics = self.rollDice(mod=dm)
        if self.mainWorldHydrographics > 10:
            self.mainWorldHydrographics = 10
        elif self.mainWorldHydrographics < 0:
            self.mainWorldHydrographics = 0
        #Population generator
        self.population = self.rollDice(mod=-2)
        #Goverment generator
        self.goverment = self.rollDice(mod=(self.population-7))
        #Lawl level generator
        self.lawLevel = self.rollDice(mod=(self.goverment-7))
        #Technological level generator
        dm = 0
        if self.starport == 'A':
            dm += 6
        elif self.starport == 'B':
            dm += 4
        elif self.starport == 'C':
            dm += 2
        elif self.starport == 'X':
            dm += -4
        if self.mainWorldSize <= 1:
            dm += 2
        elif 1 < self.mainWorldSize <= 4:
            dm += 1
        if self.mainWorldAtmosphere <= 3 or self.mainWorldAtmosphere >= 10:
            dm += 1
        if self.mainWorldHydrographics == 9:
            dm += 1
        elif self.mainWorldHydrographics == 10:
            dm += 2
        if 0 < self.population < 6:
            dm += 1
        elif self.population == 9:
            dm += 2
        elif self.population == 10:
            dm += 4
        if self.goverment == 0 or self.goverment == 5:
            dm += 1
        elif self.goverment == 13:
            dm += -2
        self.TechnologicalLevel = self.rollDice(numOfDice=1, mod=dm)


if __name__ == "__main__":
    galaxy = []
    for i in range(20):
        galaxy.append(StarSystem())
    for i in galaxy:
        print(i, '\n')