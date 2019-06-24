#!/usr/bin/python

import sys
from xmodem import YMODEM

def getc(size, timeout=1):
    return sys.stdin.read(size) or None

def putc(data, timeout=1):
    sys.stdout.write(data)

modem = YMODEM(getc, putc)

modem.send([sys.argv[1]])

