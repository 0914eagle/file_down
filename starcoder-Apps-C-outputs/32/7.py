
# coding=utf-8
# author=yphacker

s = input()

if s.count("a") == s.count("b") == s.count("c"):
    print("YES")
elif s.count("a") == s.count("c") or s.count("b") == s.count("c"):
    print("YES")
else:
    print("NO")
