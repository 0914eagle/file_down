
import sys

def get_input():
    for line in sys.stdin:
        yield line.strip()


def solve_test_case():
    n = int(next(input_iter))
    a = [int(x) for x in next(input_iter).split()]
    
    color = [0] * n
    if a.count(a[0]) == n:
        print("NO")
        return
    
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
    
    print("YES")
    for i in range(n - 1):
        print(i + 1, i + 2)


input_iter = get_input()
t = int(next(input_iter))
for _ in range(t):
    solve_test_case()

