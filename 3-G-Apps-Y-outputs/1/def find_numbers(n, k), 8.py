
def find_numbers(n, k):
    if n % 2 != k % 2 or n < k:
        return "NO"
    
    if n >= 2 * k:
        return "YES\n" + " ".join([str(n // k)] * (k - 1)) + " " + str(n - (n // k) * (k - 1))
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_numbers(n, k))
