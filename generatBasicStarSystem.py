#!Python 3

import random

def starSystemGeneration():
    starSystem = {
        'name' : '',
        'starPort' : '',
        'navelBase' : False,
        'scoutBase' : False,
        'gassGiant' : False
    }
    starPorts = ['A','A','A','B','B','C','C','D','E','E','X']
    roll = random.randint(1,6) + random.randint(1,6) - 2
    starSystem['starPort'] = starPorts[roll]
    if starSystem['starPort'] == 'C' or starSystem['starPort'] == 'D' or starSystem['starPort'] == 'E' or starSystem['starPort'] == 'X':
        starSystem['navelBase'] = False
    else:
        roll = random.randint(1,6) + random.randint(1,6)
        if roll <= 7:
            starSystem['navelBase'] = False
        else:
            starSystem['navelBase'] = True
    if starSystem['starPort'] == 'E' or starSystem['starPort'] == 'X':
        starSystem['scoutBase'] = False
    else:
        if starSystem['starPort'] == 'A':
            roll = (random.randint(1,6) + random.randint(1,6)) - 3
        elif starSystem['starPort'] == 'B':
            roll = (random.randint(1,6) + random.randint(1,6)) - 2
        elif starSystem['starPort'] == 'C':
            roll = (random.randint(1,6) + random.randint(1,6)) - 1
        else:
            roll = random.randint(1,6) + random.randint(1,6)
        if roll <= 6:
            starSystem['scoutBase'] = False
        else:
            starSystem['scoutBase'] = True
    roll = random.randint(1,6) + random.randint(1,6)
    if roll >= 10:
        starSystem['gassGiant'] = False
    else:
        starSystem['gassGiant'] = True
    spaceNameTable = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(random.randint(5,8)):
        starSystem['name'] = starSystem['name'] + spaceNameTable[random.randint(0,35)]
    #print(starSystem)
    starSystem['size'] = (random.randint(1,6) + random.randint(1,6)) - 2
    if starSystem['size'] == 0:
        starSystem['atmosphere'] = 0
    else:
        starSystem['atmosphere'] = (random.randint(1,6) + random.randint(1,6)) - 7 + starSystem['size']
    if starSystem['size'] <= 1:
        starSystem['hydrographics'] = 0
    elif starSystem['atmosphere'] >= 10 or starSystem['atmosphere'] <= 1:
        starSystem['hydrographics'] = (random.randint(1,6) + random.randint(1,6)) - 11 +  starSystem['size']
    else:
        starSystem['hydrographics'] = (random.randint(1,6) + random.randint(1,6)) - 7 +  starSystem['size']
    if starSystem['hydrographics'] > 10:
        starSystem['hydrographics'] = 10
    elif starSystem['hydrographics'] < 0:
        starSystem['hydrographics'] = 0
    starSystem['population'] = (random.randint(1,6) + random.randint(1,6)) - 2
    starSystem['goverment'] = (random.randint(1,6) + random.randint(1,6)) - 7 + starSystem['population']
    starSystem['lawLevel'] = (random.randint(1,6) + random.randint(1,6)) - 7 + starSystem['goverment']
    if starSystem['starPort'] == 'A':
        diceM = 6
    elif starSystem['starPort'] == 'B':
        diceM = 4
    elif starSystem['starPort'] == 'C':
        diceM = 2
    elif starSystem['starPort'] == 'X':
        diceM = -4
    else:
        diceM = 0
    if starSystem['size'] <= 1:
        diceM = diceM + 2
    elif 1 < starSystem['size'] <= 4:
        diceM = diceM + 1
    if starSystem['atmosphere'] <= 3 or starSystem['atmosphere'] >= 10:
        diceM = diceM + 1
    if starSystem['hydrographics'] == 9:
        diceM = diceM + 1
    elif starSystem['hydrographics'] == 10:
        diceM = diceM + 2
    if 0 < starSystem['population'] < 6:
        diceM = diceM + 1
    elif starSystem['population'] == 9:
        diceM = diceM + 2
    elif starSystem['population'] == 10:
        diceM = diceM + 4
    if starSystem['goverment'] == 0 or starSystem['goverment'] == 5:
        diceM = diceM + 1
    elif starSystem['goverment'] == 13:
        diceM = diceM -2
    starSystem['techLevel'] = random.randint(1,6) + diceM
    return starSystem


if __name__ == '__main__':
    Galixy = []
    for i in range(5):
        Galixy.append(starSystemGeneration())
    print(Galixy)