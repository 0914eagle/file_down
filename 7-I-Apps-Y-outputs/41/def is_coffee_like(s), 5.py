
def is_coffee_like(s):
    if s[2] == s[3] and s[4] == s[5]:
        return True
    return False

s = input()
print("Yes" if is_coffee_like(s) else "No")

