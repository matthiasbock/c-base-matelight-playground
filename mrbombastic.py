#!/usr/bin/python3

from random import *
from subprocess import Popen, PIPE, run
from shlex import split
from time import sleep
import socket


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

leHotMatthias = open("bild.raw", "rb").read()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    for i in range(10):
        msg = generateRandomSequence()
        sock.sendto(msg, (HOST, PORT))
        sleep(0.1)

    msg = leHotMatthias
    sock.sendto(msg, (HOST, PORT))
    sleep(3)
