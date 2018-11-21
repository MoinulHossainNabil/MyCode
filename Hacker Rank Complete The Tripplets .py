#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice=a
    bob=b
    alice_points=0
    bob_pints=0
    l=[]
    for i in range(len(alice)):
        if(alice[i]>bob[i]):
            alice_points+=1
        if(a[i]<b[i]):
            bob_pints+=1
        if(alice_points==bob_pints):
            continue
    l.append(alice_points)
    l.append(bob_pints)
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
