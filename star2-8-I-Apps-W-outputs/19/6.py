
import sys
import re
import math
import bisect
from typing import List
from io import StringIO
from collections import deque, defaultdict
def input():
    return next(sys.stdin)
def solve(s: str) -> str:
    missing_chars = set(re.findall(r'[A-Z]', s))
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if char not in missing_chars:
            return s.replace('?', char)
    return '-1'
if __name__ == '__main__':
    s = input().strip()
    print(solve(s))

