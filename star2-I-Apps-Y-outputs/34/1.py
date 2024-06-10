
import string

def solve(s):
    alphabet = set(string.ascii_lowercase)
    s_set = set(s)
    diff = alphabet - s_set
    if len(diff) == 0:
        return "None"
    return min(diff)

if __name__ == "__main__":
    s = input()
    print(solve(s))

