
import re
t = int(input())
for _ in range(t):
    s = input()
    if "010" not in s and "101" not in s:
        print(0)
    elif "010" in s and "101" in s:
        print(2)
    elif "010" in s:
        print(1)
    elif "101" in s:
        print(1)

