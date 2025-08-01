def recite(start_verse, end_verse):
    if start_verse == end_verse:
        return [recite_single(start_verse)]
    return [recite_single(x) for x in range(start_verse, end_verse+1)]

def recite_single(verse):
    days = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth",
    }
    things = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "a Partridge in a Pear Tree.",
    ]
    things.reverse()
    if verse > 1:
        things[0] = "and a Partridge in a Pear Tree."
    intro = "On the {} day of Christmas my true love gave to me: ".format(days[verse])
    return intro + "".join(reversed(things[0:verse]))





expected = [
            "On the first day of Christmas my true love gave to me: "
            "a Partridge in a Pear Tree."
        ]
print(recite(1, 1), expected)