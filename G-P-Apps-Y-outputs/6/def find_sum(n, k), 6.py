
def find_sum(n, k):
    if n % 2 != k % 2:
        return "NO"
    elif n < k:
        return "NO"
    else:
        return "YES\n" + " ".join([str(n//k)]*k)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_sum(n, k))
