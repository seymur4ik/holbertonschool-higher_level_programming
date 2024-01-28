#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            s = chr(ord(c) - 32)
        else:
            s = c
        print("{}".format(s), end="")
    print("")
