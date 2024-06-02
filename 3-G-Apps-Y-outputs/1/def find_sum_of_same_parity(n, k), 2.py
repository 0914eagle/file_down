
def find_sum_of_same_parity(n, k):
    if n % 2 != k % 2 or n < k:
        return "NO"
    
    if k == 1:
        return "YES\n{}".format(n)
    
    if n % 2 == 0:
        return "YES\n" + " ".join(["{}".format(n // k)] * k)
    else:
        return "YES\n" + " ".join(["{}".format((n - k + 1) // k)] * (k - 1)) + " {}".format(n - (k - 1) * ((n - k + 1) // k))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_sum_of_same_parity(n, k))
