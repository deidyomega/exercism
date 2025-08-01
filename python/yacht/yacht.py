"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"
YACHT = "YACHT"

def same(lst):
    return len(set(lst)) == 1

def score(dice, category):
    dice = sorted(dice)

    # ONES, TWOS...
    if category in range(1, 7):
        return dice.count(category) * category

    if category == YACHT:
        return 50 if dice[0] == dice[4] else 0
    if category == LITTLE_STRAIGHT:
        return 30 if dice == [1, 2, 3, 4, 5] else 0
    if category == BIG_STRAIGHT:
        return 30 if dice == [2, 3, 4, 5, 6] else 0
    if category == CHOICE:
        return sum(dice)

    if category == FULL_HOUSE:
        if dice[0] == dice[4]:
            return 0
        if same(dice[0:3]) and same(dice[3:6]):
            return sum(dice)
        if same(dice[0:2]) and same(dice[2:6]):
            return sum(dice)
        return 0
    
    if category == FOUR_OF_A_KIND:
        if same(dice[0:4]):
            return dice[0] * 4
        if same(dice[1:5]):
            return dice[4] * 4
        return 0

