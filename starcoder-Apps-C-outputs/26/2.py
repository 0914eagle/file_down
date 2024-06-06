
import re
def packman(s):
    a = re.findall(r"\*+", s)
    return max(len(x) for x in a)

n = int(input())
s = input()
print(packman(s))
