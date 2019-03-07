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

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    print("video...")
    for i in range(218):
        print("frame {:d}...".format(i))
        f = open("{:03d}.jpg.rgb".format(i+1), "rb")
        stretched = b""
        pixel = 24
        a = int((40-pixel)/2)
        b = 40-pixel-a
        for row in range(16):
            stretched += bytes(a*3) + f.read(pixel*3) + bytes(b*3)
        f.close() 
        msg = stretched
        sock.sendto(msg, (HOST, PORT))
        sleep(0.1)
