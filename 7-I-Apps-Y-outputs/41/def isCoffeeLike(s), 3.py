
def isCoffeeLike(s):
    return s[2] == s[3] and s[4] == s[5]

s = input()
print("Yes" if isCoffeeLike(s) else "No")
