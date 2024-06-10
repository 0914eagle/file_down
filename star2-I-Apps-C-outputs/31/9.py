
from sys import stdin
input = stdin.readline

def solve():
    n, m = map(int, input().split())
    words = [input().split() for _ in range(n)]
    letters = set()
    for word in words:
        for letter in word:
            letters.add(int(letter))
    print("Yes")
    print(len(letters))
    print(" ".join(map(str, sorted(letters))))

solve()

