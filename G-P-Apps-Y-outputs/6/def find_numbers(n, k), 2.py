
def find_numbers(n, k):
    if k > n or (n % 2 != k % 2):
        return "NO"
    else:
        return "YES\n" + " ".join([str(n // k)] * (k-1)) + " " + str(n - (n // k) * (k-1))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_numbers(n, k))
