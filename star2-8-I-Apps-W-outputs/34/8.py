
import re
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if re.search("010|101", s):
        print(1)
    else:
        print(0)

