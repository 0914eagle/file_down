

import sys

test = int(sys.stdin.readline().strip())

for _ in range(test):
    s = sys.stdin.readline().strip()
    
    if s.endswith("po"):
        print("FILIPINO")
    elif s.endswith("desu") or s.endswith("masu"):
        print("JAPANESE")
    elif s.endswith("mnida"):
        print("KOREAN")
