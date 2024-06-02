
def solve_test_case(n, k):
    if n % 2 != k % 2 or n < k:
        print("NO")
    else:
        if n % 2 == 0:
            print("YES")
            print(" ".join(["2"] * (k-1) + [str(n - 2*(k-1))]))
        else:
            if k == 1:
                print("NO")
            else:
                print("YES")
                print(" ".join(["1"] * (k-1) + [str(n - (k-1))]))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    solve_test_case(n, k)
