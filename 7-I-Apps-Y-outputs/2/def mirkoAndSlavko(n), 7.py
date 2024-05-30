
import math
import os
import random
import re
import sys

#
# Complete the 'mirkoAndSlavko' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def mirkoAndSlavko(n):
    # Write your code here
    return n//2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = mirkoAndSlavko(n)

    fptr.write(str(result) + '\n')

    fptr.close()

