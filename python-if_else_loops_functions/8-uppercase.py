#!/usr/bin/python3
def uppercase(str):
    for item in range(len(str)):
        if ord(str[item]) >= ord('a') and ord(str[item]) <= ord('z'):
            atoi = ord(str[item]) + (ord('A') - ord('a'))
        else:
            atoi = ord(str[item])
        print("{}".format(chr(atoi)), end='')
    print()
