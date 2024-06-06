
def func_462a6756573347579741371733f53306(n, m):
    a = list(map(int, input().split()))
    cur_max = 0
    for i in range(m):
        if a[i] > cur_max:
            cur_max = a[i]
    if cur_max <= n:
        print(cur_max)
    else:
        print(0)


if __name__ == '__main__':
    n, m = map(int, input().split())
    func_462a6756573347579741371733f53306(n, m)
