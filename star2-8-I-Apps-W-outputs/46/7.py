
def solve(h_sizes, b_sizes):
    for h_num in h_sizes:
        for b_num in b_sizes:
            if h_num % b_num == 0:
                return 2
            if b_num % h_num == 0:
                return 2
            if h_num - b_num in b_sizes or b_num - h_num in h_sizes:
                return 2
    return "impossible"

h_num = int(input())
h_sizes = list(map(int, input().split()))
b_num = int(input())
b_sizes = list(map(int, input().split()))

print(solve(h_sizes, b_sizes))

