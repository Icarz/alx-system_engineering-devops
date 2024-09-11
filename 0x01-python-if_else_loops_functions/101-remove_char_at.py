#!/usr/bin/python3
def remove_char_at(str, n):
    strmp = ""
    cont = 0
    for c in str:
        if cont == n:
            pass
        else:
            strmp += c
        cont += 1
    return strmp
