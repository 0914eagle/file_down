


import sys

def main() -> None:
    def print(*args, **kwargs):
        
        sys.stdout.write(''.join(str(a) for a in args) + '\n')
    
    def read():
        return sys.stdin.readline().rstrip()

    def read_int():
        return int(sys.stdin.readline())

    def read_ints():
        return [int(x) for x in sys.stdin.readline().split()]
    
    def read_ints_as_str():
        return [x for x in sys.stdin.readline().split()]

    nrow, ncol, num, keep = read_ints()
    m = []
    for _ in range(num + keep):
        m.append(tuple(read_ints()))
    m = sorted(m)
    l = []
    for _ in range(num):
        l.append(m[_])
    for _ in range(num, num+keep):
        l.append(m[_])

    i = 0
    ans = 0
    for _ in l:
        x = _
        if x[0] < nrow and x[1] < ncol:
            if i == 0:
                ans += 1
            else:
                pre = l[i-1]
                if x[0] < pre[0] and x[1] >= pre[1] or x[0] <= pre[0] and x[1] < pre[1]:
                    ans += 1
                else:
                    ans += 2
        else:
            ans += 1
        i += 1
    print(ans)

if __name__ == "__main__":
    main()


