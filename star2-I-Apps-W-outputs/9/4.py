
def solve(t, s):
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    t = [tuple(map(int, x.split('-'))) for x in input().split()]
    s = [tuple(map(int, x.split('-'))) for x in input().split()]
    print(solve(t, s))

