#!/usr/bin/python

import sys
from xmodem import YMODEM

import logging
logging.basicConfig()

debug=False
bytes_sent=0

def getc(size, timeout=1):
    data = sys.stdin.read(size)
    if debug:
        sys.stderr.write("read "+repr(data)+"\n")
    return data or None

def putc(data, timeout=1):
    global bytes_sent
    bytes_sent += len(data)
    sys.stderr.write("sent "+str(bytes_sent/1024)+"kB\r")
    if debug:
        sys.stderr.write("write "+str(bytes_sent)+":"+repr(data)+"\n")
    sys.stdout.write(data)

modem = YMODEM(getc, putc)

modem.send([sys.argv[1]])

