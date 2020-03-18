url="https://www.hackerrank.com/challenges/2d-array/problem?h_r=next-challenge&h_v=zen"
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sm=0
    for i in range(0,4):
        for j in range(0,4):
            s=0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if(k==(i+1)):
                        if(l==j or l==(j+2)):
                            pass
                        else:
                            s=s+arr[k][l]
                    else:
                        s=s+arr[k][l]    
            if(s>sm):
                sm=s
            print(s)
    return sm
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #arr = []

    #for _ in range(6):
        #arr.append(list(map(int, input().rstrip().split())))
    arr=[[0,-4,-6,0,-7,-6],[-1,-2,-6,-8,-3,-1],[-8,-4,-2,-8,-8,-6],[-3,-1,-2,-5,-7,-4],[-3,-5,-3,-6,-6,-6],[-3,-6,0,-8,-6,-7]]
    result = hourglassSum(arr)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()