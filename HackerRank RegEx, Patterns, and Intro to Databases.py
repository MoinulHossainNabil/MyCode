#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    check = '@gmail.com'
    output = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if check in emailID:
            output.append(firstName)
    result = sorted(output)
    for i in result:
        print(i)
