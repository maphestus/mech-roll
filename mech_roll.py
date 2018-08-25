import dice

class Mech:
    """One mech instance"""
    mechCount = 0

    def __init__(self, name, size, armor, wound):
        self.name = name
        self.size = size
        self.armor = armor
        self.wound = wound


def dice_roller(d):
    tot = 0
    a = dice.roll(str(d) + 'd10')
    for success in a:
        if success >= 7:
            tot += 1
    print(a)
    return tot


def hit_location():
    loc = dice.roll('d20')
    loc = loc[0]
    print(loc)
    if loc == 20:
        print('Head')
        loc = 0
    elif loc >= 17 and loc <= 19:
        print('Left Arm')
        loc = 1
    elif loc >= 14 and loc <= 16:
        print('Right Arm')
        loc = 2
    elif loc >= 7 and loc <= 13:
        print('Torso')
        loc = 3
    elif loc >= 4 and loc <= 6:
        print('Left Leg')
        loc = 4
    elif loc >= 1 and loc <= 3:
        print('Right Leg')
        loc = 5
    else:
        print('Blah')
    return loc

def printmech(mech):
    mech_string = f"""      {mech.armor[0]}/{mech.wound[0]}
{mech.armor[1]}/{mech.wound[1]}   {mech.armor[3]}/{mech.wound[3]}   {mech.armor[2]}/{mech.wound[2]}
   {mech.armor[4]}/{mech.wound[4]}   {mech.armor[5]}/{mech.wound[5]}
"""
    print(mech.name)
    print(mech_string)
    return


def battle(mech1, mech2):
    print("Battle Commence!")
    hit_loc = hit_location()
    dmg = dice_roller(4)
    print("Mech hit location:", hit_loc)
    print("Total Successes: ", dmg)
    if mech2.armor[hit_loc] > 0:
        print("Armor Hit!")
        if dmg < mech2.armor[hit_loc]:
            print("Didn't Penetrate", mech2.armor[hit_loc])
            return
        elif dmg == mech2.armor[hit_loc]:
            print("Armor Damaged!")
            mech2.armor[hit_loc] = mech2.armor[hit_loc] - 1
            return
        elif dmg > mech2.armor[hit_loc]:
            print("Armor Breach!")
            pen = dmg - mech2.armor[hit_loc]
            mech2.wound[hit_loc] = mech2.wound[hit_loc] - pen
            mech2.armor[hit_loc] = mech2.armor[hit_loc] - 1
            return




#mech1 = ('Baphomet', 'S', [0,1,1,2,1,1], [1,1,1,1,1,1])
#mech2 = ('Falstaff', 'S', [0,1,1,2,1,1], [1,1,1,1,1,1])

mech1 = Mech('Baphomet', 'S', armor = [1, 1, 1, 2, 1, 1], wound = [1, 1, 1, 2, 1, 1])

mech2 = Mech('Falstaff', 'S', armor = [0, 1, 1, 2, 1, 1], wound = [1, 1, 1, 1, 1, 1])

#print(mech1)
#print(mech2)

#print(dice_roller(2))
#print(hit_location())
battle(mech1, mech2)

printmech(mech1)
printmech(mech2)



