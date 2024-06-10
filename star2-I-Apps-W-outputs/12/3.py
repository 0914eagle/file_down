
from collections import Counter
def solve(s):
    s = s.replace('?', ' ')
    counter = Counter(s)
    if len(counter) < 26:
        return -1
    missing_letters = [ch for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if ch not in counter]
    for ch in missing_letters:
        s = s.replace(' ', ch, 1)
    return s

if __name__ == '__main__':
    s = input()
    print(solve(s))

