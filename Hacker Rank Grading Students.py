#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
# My Piece Of Code!!
def gradingStudents(grades):
    #
    # Write your code here.
    #r=1
    result=[]
    for g in grades:
        n=g
        if(g>=38):
            while(g%5!=0):
                #r=g%5
                g+=1
            diff=g-n
            if(diff<3):
                result.append(g)
            else:
                result.append(n)
        else:
            result.append(g)
    return result
# Hacker Rank Default Code Section
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
