#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
# My Piece Of Code!!
def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apple=0
    total_orange=0
    for appel in range(len(apples)):
        tempapple=a+apples[appel]
        if(tempapple>=s and tempapple<=t):
            total_apple+=1
    for orange in range(len(oranges)):
        temporange=b+oranges[orange]
        if(temporange>=s and temporange<=t):
            total_orange+=1
    print(total_apple)
    print(total_orange)

# Hacker Rank Default Code Section
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
