
def is_coffee_like(s):
    return s[2] == s[3] and s[4] == s[5]


s = input()
print("Yes" if is_coffee_like(s) else "No")

