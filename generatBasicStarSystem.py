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
    roll = random.randint(1,6) + random.randint(1,6)
    starSystem['starPort'] = starPorts[roll-1]
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
    print(starSystem)
    starSystem['size'] = (random.randint(1,6) + random.randint(1,6)) - 2
    if starSystem['size'] == 0:
        starSystem['atmosphere'] = 0
    else:
        starSystem['atmosphere'] = (random.randint(1,6) + random.randint(1,6)) - 7 + starSystem['size']
    if starSystem['size'] == 1:
        starSystem


if __name__ == '__main__':
    for b in range(5):
        newStarSystem = starSystemGeneration()