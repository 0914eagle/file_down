
from string import ascii_lowercase

def solve(s):
    for c in ascii_lowercase:
        if c not in s:
            return c
    return None

if __name__ == '__main__':
    s = input()
    print(solve(s))

