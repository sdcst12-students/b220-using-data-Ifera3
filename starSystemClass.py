#!Python 3

import random

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

    def starportLookUpTable(self):
        if self.starport == "A":
            return "Excellent quality starport with refined fuel, overhaul, shipyards."
        elif self.starport == "B":
            return "Good quality starport with refined fuel, overhaul, shipyards for non-starships."
        elif self.starport == "C":
            return "Routine quality starport with unrefined fuel, some repair facilities."
        elif self.starport == "D":
            return "Poor quality starport with unrefined fuel; no repair facilities."
        elif self.starport == "E":
            return "Starport is a frontier installation; no facilities."
        elif self.starport == "X":
            return "No starport."

    def mainWorldSizeLookUpTable(self):
        if self.mainWorldSize <= 0:
            return "Asteriod/Planetiod Belt"
        elif self.mainWorldSize == 1:
            return "1,000 miles(1 600 km)"
        elif self.mainWorldSize == 2:
            return "2,000 miles(3 200 km)"
        elif self.mainWorldSize == 3:
            return "3,000 miles(4 800 km)"
        elif self.mainWorldSize == 4:
            return "4,000 miles(6 400 km)"
        elif self.mainWorldSize == 5:
            return "5,000 miles(8 000 km)"
        elif self.mainWorldSize == 6:
            return "6,000 miles(9 600 km)"
        elif self.mainWorldSize == 7:
            return "7,000 miles(11 200 km)"
        elif self.mainWorldSize == 8:
            return "8,000 miles(12 800 km)"
        elif self.mainWorldSize == 9:
            return "9,000 miles(14 400 km)"
        elif self.mainWorldSize >= 10:
            return "10,000 miles(16 000 km)"

    def mainWorldAtmosphereLookUpTable(self):
        if self.mainWorldAtmosphere <= 0:
            return "No atmosphere."
        elif self.mainWorldAtmosphere == 1:
            return "Trace."
        elif self.mainWorldAtmosphere == 2:
            return "Very thin, tainted."
        elif self.mainWorldAtmosphere == 3:
            return "Very thin."
        elif self.mainWorldAtmosphere == 4:
            return "Thin, tainted."
        elif self.mainWorldAtmosphere == 5:
            return "Thin."
        elif self.mainWorldAtmosphere == 6:
            return "Standered."
        elif self.mainWorldAtmosphere == 7:
            return "Standered, tainted."
        elif self.mainWorldAtmosphere == 8:
            return "Dense."
        elif self.mainWorldAtmosphere == 9:
            return "Dense, Tainted."
        elif self.mainWorldAtmosphere == 10:
            return "Exotic."
        elif self.mainWorldAtmosphere == 11:
            return "Corrosive."
        elif self.mainWorldAtmosphere == 12:
            return "Insidious."
        elif self.mainWorldAtmosphere == 13:
            return "Dense, high."
        elif self.mainWorldAtmosphere == 14:
            return "Ellipsoid"
        elif self.mainWorldAtmosphere >= 15:
            return "Thin, low."

    def mainWorldHydrographicsLookUpTable(self):
        if self.mainWorldHydrographics <= 0:
            return "No free standing water."
        elif self.mainWorldHydrographics == 1:
            return "10% water."
        elif self.mainWorldHydrographics == 2:
            return "20% water."
        elif self.mainWorldHydrographics == 3:
            return "30% water."
        elif self.mainWorldHydrographics == 4:
            return "40% water."
        elif self.mainWorldHydrographics == 5:
            return "50% water."
        elif self.mainWorldHydrographics == 6:
            return "60% water."
        elif self.mainWorldHydrographics == 7:
            return "70% water."
        elif self.mainWorldHydrographics == 8:
            return "80% water."
        elif self.mainWorldHydrographics == 9:
            return "90% water."
        elif self.mainWorldHydrographics == 10:
            return "No land masses."

    def populationLookUpTable(self):
        if self.population <= 0:
            return "No inhabitans."
        elif self.population == 1:
            return "Tens of inhabitans."
        elif self.population == 2:
            return "Hundreds of inhabitans."
        elif self.population == 3:
            return "Thousands of inhabitans."
        elif self.population == 4:
            return "Tens of thousands."
        elif self.population == 5:
            return "Hundreds of thousands."
        elif self.population == 6:
            return "Millions of inhabitans."
        elif self.population == 7:
            return "Tens of millions."
        elif self.population == 8:
            return "Hundreds of millions."
        elif self.population == 9:
            return "Billions of inhabitans."
        elif self.population >= 10:
            return "Tens of billions."

    def govermentLookUpTable(self):
        if self.goverment <= 0:
            return "No goverment struture."
        elif self.goverment  == 1:
            return "Company/Corparation."
        elif self.goverment  == 2:
            return "Participating Democracy."
        elif self.goverment  == 3:
            return "Self-Perpatuating Oligarchy."
        elif self.goverment  == 4:
            return "Representative Democracy."
        elif self.goverment  == 5:
            return "Feudal Technocracy."
        elif self.goverment  == 6:
            return "Captive Goverment."
        elif self.goverment  == 7:
            return "Balkanization."
        elif self.goverment  == 8:
            return "Civil Service Bureaucracy."
        elif self.goverment  == 9:
            return "Impersonal Bureaucracy."
        elif self.goverment  == 10:
            return "Charismatic Dictator."
        elif self.goverment  == 11:
            return "Non-Charismatic Leader."
        elif self.goverment  == 12:
            return "Charismatic Oligarchy."
        elif self.goverment  == 13:
            return "Religious Dictatorship."

    def lawLevelLookUpTable(self): 
        if self.lawLevel <= 0:
            return "No prohibitions. "
        result = ""
        if self.lawLevel >= 1:
            result += "Body pistols undetectable by standard detectors, explosives, and poison gas prohibited. "
        if self.lawLevel >= 2:
            result += "Portable ebergy weapons prohibited. "
        if self.lawLevel >= 3:
            result += "Weapons of a strict military nature prohibited. "
        if self.lawLevel >= 4:
            result += "Light assault weapons prohibited. "
        if self.lawLevel >= 5:
            result += "Personal concealable firearms prohibited. "
        if self.lawLevel >= 6:
            result += "Most firearms prohibited. The carrying of any type of weapon is discouraged. "
        if self.lawLevel >= 7:
            result += "Shotguns are prohibited. "
        if self.lawLevel >= 8:
            result += "Long bladed weapons are controlled, and open possession is prohibited. "
        if self.lawLevel >= 9:
            result += "Possesion of any weapon outside one's residance is prohibited. "
        if self.lawLevel >= 10:
            result += "Possession of any weapon is prohibited. "
        return result

    def TechnologicalLevelLookUpTable(self):
        if self.TechnologicalLevel <= 0:
            return "Stone Age or Primitive."
        elif self.TechnologicalLevel == 1:
            return "Bronze Age to Middle Ages."
        elif self.TechnologicalLevel == 2:
            return "Circa 1400 to 1700."
        elif self.TechnologicalLevel == 3:
            return "Circa 1700 to 1860."
        elif self.TechnologicalLevel == 4:
            return "Circa 1860 to 1900."
        elif self.TechnologicalLevel == 5:
            return "Circa 1900 to 1939."
        elif self.TechnologicalLevel == 6:
            return "Circa 1940 to 1969."
        elif self.TechnologicalLevel == 7:
            return "Circa 1970 to 1979."
        elif self.TechnologicalLevel == 8:
            return "Circa 1980 to 1989."
        elif self.TechnologicalLevel == 9:
            return "Circa 1990 to 2000."
        elif self.TechnologicalLevel == 10:
            return "Interstellar community."
        elif self.TechnologicalLevel == 11 or self.TechnologicalLevel == 12:
            return "Average Imperial."
        elif self.TechnologicalLevel == 13 or self.TechnologicalLevel == 14:
            return "Above average Imperial"
        elif self.TechnologicalLevel == 15:
            return "Technical maximum Imperial"
        elif self.TechnologicalLevel >= 16:
            return "Occasional non-Imperial"

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
        return f"Star system {self.name}. Starport: {self.starportLookUpTable()} {waterbase} {gas} Main world size: {self.mainWorldSizeLookUpTable()} Main world atmosphere: {self.mainWorldAtmosphereLookUpTable()} Main world Hydrograhics: {self.mainWorldHydrographicsLookUpTable()} Population: {self.populationLookUpTable()} Goverment: {self.govermentLookUpTable()} Laws: {self.lawLevelLookUpTable()}Technological level: {self.TechnologicalLevelLookUpTable()}"

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