
def solve():
    n = int(input())
    s = input()
    t = ''
    for i in range(n):
        if i == 0:
            t += s[i]
        else:
            if s[i] == t[-1]:
                if s[i] == 'R':
                    t += 'G'
                elif s[i] == 'G':
                    t += 'B'
                else:
                    t += 'R'
            else:
                t += s[i]
    print(n - t.count(t[0]))
    print(t)

solve()

