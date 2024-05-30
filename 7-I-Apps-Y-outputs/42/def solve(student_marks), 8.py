
import sys
import re
import math
import os
import json
import time
import string
import random
import csv
import numpy as np
import collections

def solve(student_marks):
    # Enter your code here
    return sum(student_marks)/len(student_marks)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    student_marks = []
    for _ in range(int(input())):
        line = input().split()
        student_marks.append(float(line[1]))
    res = solve(student_marks)
    fptr.write('%.2f' % res + '\n')
    fptr.close()

