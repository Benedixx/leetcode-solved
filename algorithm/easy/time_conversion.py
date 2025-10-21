#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    med_time = s[-2:]
    time = s[:-2].split(":")
    
    if med_time == "PM":
        if time[0] == "12":
            pass
        else:
            time[0] = int(time[0]) + 12  
    elif med_time == "AM":
        if time[0] == "12":
            time[0] = "00"
        
    return f"{time[0]}:{time[1]}:{time[2]}"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
