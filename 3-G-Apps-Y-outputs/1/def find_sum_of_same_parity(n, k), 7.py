
def find_sum_of_same_parity(n, k):
    if n % 2 == 0:
        if k % 2 == 0:
            return "YES\n" + " ".join([str(n // k)] * k)
        elif k <= n and k % 2 == 1:
            return "YES\n" + " ".join([str(1)] * (k - 1)) + " " + str(n - (k - 1))
    else:
        if k % 2 == 1:
            return "YES\n" + " ".join([str(1)] * k)
    return "NO"

# Input reading
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_sum_of_same_parity(n, k))
