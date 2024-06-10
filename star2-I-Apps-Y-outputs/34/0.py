
import string

def solve(s):
    alphabet = set(string.ascii_lowercase)
    s = set(s)
    diff = alphabet - s
    if len(diff) == 0:
        return "None"
    else:
        return min(diff)

if __name__ == "__main__":
    s = input()
    print(solve(s))

