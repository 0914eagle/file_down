
s=input()
if "a" in s or "e" in s or "i" in s or "o" in s or "u" in s:
    if "n" not in s:
        print("YES")
    elif s.endswith("n"):
        print("YES")
    else:
        print("NO")
