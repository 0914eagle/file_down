
from sys import stdin

def rebus(s):
    s = s.strip()
    if len(s) < 2:
        return "Impossible"
    s = s.split(" ")
    s = [x for x in s if x != ""]
    n = int(s[-1])
    if "+" in s:
        i = s.index("+")
        if i == 1:
            return "Impossible"
        a = int(s[i-1])
        b = n - int(s[i+1])
        if b < 0:
            return "Impossible"
        return "{} + {} = {}".format(a, b, n)
    elif "-" in s:
        i = s.index("-")
        if i == 1:
            return "Impossible"
        a = int(s[i-1])
        b = n + int(s[i+1])
        if b < 0:
            return "Impossible"
        return "{} - {} = {}".format(b, a, n)
    else:
        return "Impossible"

for line in stdin:
    print(rebus(line))

