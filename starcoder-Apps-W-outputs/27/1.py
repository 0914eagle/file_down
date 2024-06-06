
def solution():
    def judge(letters, s, t):
        for a, b in zip(s, t):
            if a == b:
                continue
            return letters.index(a) < letters.index(b)
        return len(s) < len(t)

    from itertools import permutations
    n = int(input())
    names = [input() for i in range(n)]
    for letters in permutations('abcdefghijklmnopqrstuvwxyz'):
        if all(judge(letters, s, t) for s, t in zip(names, names[1:])):
            print(''.join(letters))
            return
    print('Impossible')


if __name__ == '__main__':
    solution()
