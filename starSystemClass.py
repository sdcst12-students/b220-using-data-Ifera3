#!Python 3

import random

class StarSystem():
    name = ""
    starport = "X"
    navelBase = False
    scoutBase = False
    gasGiatnt = False
    mainWorldSize = 0
    mainWorldAtmosphere = 0
    mainWorldHydrographics = 0
    population = 0
    goverment = 0
    lawLevel = 0
    TechnologicalLevel = 0

    def rollDice(self, mod=0, numOfDice=2):
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
            return ""

    def __init__(self):
        spaceNameTable = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
        for i in range(random.randint(5,8)):
            self.name += spaceNameTable[random.randint(0,36)]
        self.name = self.name.strip()
        starPorts = ['A','A','A','B','B','C','C','D','E','E','X']
        self.starport = starPorts[self.rollDice(-2)]
        if self.starport != 'C' and self.starport != 'D' and self.starport != 'E' and self.starport != 'X':
            if self.rollDice() >= 8:
                self.navelBase = True
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
        if self.rollDice() <= 9:
            self.gasGiatnt = True
        self.mainWorldSize = self.rollDice(mod=-2)
        if self.mainWorldSize == 0:
            self.mainWorldAtmosphere = 0
        else:
            self.mainWorldAtmosphere = self.rollDice(mod=(self.mainWorldSize-7))
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
        self.population = self.rollDice(mod=-2)
        self.goverment = self.rollDice(mod=(self.population-7))
        self.lawLevel = self.rollDice(mod=(self.goverment-7))
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
        print(galaxy[i].mainWorldSizeLookUpTable())
    