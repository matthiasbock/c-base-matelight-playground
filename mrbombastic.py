#!/usr/bin/python3

from random import *

LENGTH=640
PADDING=4

def getRandom():
    return int(random()*256)

def getColor():
    r = getRandom()
    g = getRandom()
    b = getRandom()
    return (r,g,b)

def generateRandomSequence():
    sequence = ""
    for i in range(LENGTH):
        c = getColor()
        sequence += chr(c[0]) + chr(c[1]) + chr(c[2])
    for i in range(PADDING):
        sequence += chr(0)
    return sequence

#if __name__ == "__main__":
seed()

print(generateRandomSequence())

