#!/usr/bin/python3
def uppercase(str):
    strmp = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            strmp += chr(ord(c)-32)
        else:
            strmp += c
    print("{}".format(strmp))
