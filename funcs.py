import math


def levelxp(level):
    level = int(level)
    xp = (((math.floor(level / 10) + 1) * 100) * (level % 10))+(pow(math.floor(level / 10), 2) + math.floor(level / 10)) * 500
    return xp


def fromto(fromLvl, toLvl):
    if toLvl > fromLvl:
        fromXp = levelxp(fromLvl)
        toXp = levelxp(toLvl)
        return toXp - fromXp
    else:
        return 0
