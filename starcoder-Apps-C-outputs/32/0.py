

import re

def check(s):
    if re.findall(r"a+b+c+|b+a+c+|c+a+b+|a+c+b+|b+c+a+|c+b+a+",s):
        return True
    return False

if __name__ == "__main__":
    s = input()
    print("YES" if check(s) else "NO")
