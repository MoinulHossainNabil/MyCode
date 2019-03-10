#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mx,mn=scores[0],scores[0]
    maxcount,mincount=0,0
    res=[]
    for i in scores:
        if(i>mx):
            mx=i
            maxcount+=1
        if(i<mn):
            mn=i
            mincount+=1
    res.append(maxcount)
    res.append(mincount)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
