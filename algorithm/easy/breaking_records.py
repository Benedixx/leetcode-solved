#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    cur_max_score = scores[0]
    cur_least_score = scores[0]
    records = [0, 0]
    for score in scores:
        if score < cur_least_score:
            cur_least_score = score
            records[1] = records[1] + 1
            print(f"change least score cur:{cur_least_score}, {score}")
        elif score > cur_max_score:
            cur_max_score = score
            records[0] = records[0] + 1
            print(f"change max score cur:{cur_max_score}, {score}")
        else:
            print(f"skip: {score}")
            continue
            
    return records 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
