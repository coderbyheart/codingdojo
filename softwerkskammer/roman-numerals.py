# -*- coding: utf-8 -*-
#
# Roman Numerals Dojo
#
# @author Pavlos Giannakis <pvlsgnnks@googlemail.com>
# @author Markus Tacker <m@coderbyheart.de>
#
# TODO:
#   Korrekte Umsetzung der Subtraktionsregel: man hat die Wahl zwischen zwei
#   Zeichen (dem kleineren, oder dem größeren)
#

# Zeichen initialisieren
a2r = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M')]

def arabic_to_roman(arabic):
    """Konvertiert eine arabische Zahl in eine römische Zahl"""
    global a2r

    # Null oder negative Zahlen gibt es nicht
    if arabic <= 0:
        return  ""

    rom = ""

    # Finde die beiden römischen Zeichen die am nächsten zur Zahl stehen
    prev = a2r[0]
    for ky in range(len(a2r)-1):
        k = a2r[ky]
        if k[0] > arabic:
            break
        prev = k
    next_rom = k[1]
    prev_rom = prev[1]

    diff = k[0] - arabic
    if diff == prev[0]: # Differenz ist gleich dem kleineren Zeichen
        if diff == 5: # Sonderfall
            rom = prev_rom + arabic_to_roman(arabic - 5)
        else:
            rom = prev_rom + next_rom
    elif diff == 1:
        rom = arabic_to_roman(diff) + next_rom
    else:
        rom = prev_rom + arabic_to_roman(arabic - prev[0])
    
    return rom

def atr(arabic):
    """Shorthand für arabic_to_roman"""
    return arabic_to_roman(arabic)

def assertRoman(exprom, arab, msg=None):
    """Hilfsmethode für den Unit-Test"""
    gotrom = atr(arab)
    themsg = "Expected %s, got %s for %d" % (exprom, gotrom, arab)
    if msg != None:
        themsg += msg
    if (exprom != gotrom):
        raise Exception(themsg)
    print "%d = %s" % (arab, exprom) 

if __name__ == "__main__":
    assertRoman("I", 1)
    assertRoman("II", 2)   
    assertRoman("III", 3)
    assertRoman("IV", 4)
    assertRoman("V", 5)
    assertRoman("VI", 6)
    assertRoman("VII", 7)
    assertRoman("VIII", 8)
    assertRoman("IX", 9)
    assertRoman("X", 10)
    assertRoman("XI", 11)
    assertRoman("XII", 12)
    assertRoman("XIII", 13)
    assertRoman("XIV", 14)
    assertRoman("XV", 15)
    assertRoman("XVI", 16)
    assertRoman("XVII", 17)
    assertRoman("XVIII", 18)
    assertRoman("XIX", 19)
    assertRoman("XX", 20)
    assertRoman("XXI", 21)
    assertRoman("XXV", 25)
    assertRoman("XXXI", 31)
    assertRoman("XXXII", 32)
    assertRoman("XXXIII", 33)
    assertRoman("XXXIV", 34)
    assertRoman("XXXV", 35)
    assertRoman("XXXVI", 36)
    assertRoman("XXXVII", 37)
    assertRoman("XXXVIII", 38)
    assertRoman("XXXIX", 39)
    assertRoman("XL", 40)
    # TODO
    assertRoman("XLIX", 49)
    assertRoman("XC", 90)
    assertRoman("XCV", 95)
    assertRoman("XCIX", 99)
    assertRoman("MCMLXXXIV", 1984)
