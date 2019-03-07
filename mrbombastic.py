#!/usr/bin/python3

from random import *
from subprocess import Popen, PIPE, run
from shlex import split

LENGTH=640
PADDING=4
HOST="api.matelight.rocks"
PORT=1337

def getRandom():
    return int(random()*256).to_bytes(1, byteorder="big")

def getRandomColor():
    r = getRandom()
    g = getRandom()
    b = getRandom()
    return (r,g,b)

def generateRandomSequence():
    sequence = b""
    for i in range(LENGTH):
        c = getRandomColor()
        sequence += c[0] + c[1] + c[2]
    for i in range(PADDING):
        sequence += b"\0"
    return sequence

#if __name__ == "__main__":
seed()

data = generateRandomSequence()
print("Sequence length is {:d}".format(len(data)))

f=open("datei","wb")
f.write(data)
f.close()

cmd = split("netcat -u {:s} {:d}".format(HOST, PORT))
p = Popen(cmd, stdin=PIPE)
p.communicate(input = data)
p.terminate()
#p.wait()

#run(cmd, stdout=PIPE, input=generateRandomSequence(), encoding="utf-8")

#print(generateRandomSequence())

