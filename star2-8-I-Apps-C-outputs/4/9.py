
import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    min_a = 10001
    min_b = 10001
    min_c = 10001
    for j in range(N):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        min_a = min(min_a, a)
        min_b = min(min_b, b)
        min_c = min(min_c, c)
    min_total = min(min_a + min_b + min_c, 10000)
    max_like = 0
    for j in range(min_total + 1):
        for k in range(min_total - j + 1):
            if j + k <= min_a and j + k <= min_b and j + k <= min_c:
                max_like += 1
    print(f"Case #{i + 1}: {max_like}")

