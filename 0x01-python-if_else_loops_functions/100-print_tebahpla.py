#!/usr/bin/python3
strmp = ""
for i in reversed(range(97, 123)):
    if (i % 2) == 0:
        strmp += chr(i)
    else:
        strmp += chr(i-32)
print("{}".format(strmp), end="")
