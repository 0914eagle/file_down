
def find_sum_of_same_parity(n, k):
    if n % 2 != k % 2:
        return "NO"
    
    if n < k:
        return "NO"
    
    if n < 2 * k:
        return "NO"
    
    if k == 1:
        return "YES\n{}".format(n)
    
    if n % 2 == 0:
        return "YES\n" + " ".join(["1"] * (k - 1) + [str(n - k + 1)])
    else:
        return "YES\n" + " ".join(["1"] * (k - 2) + [str(n - k + 2), "1"])

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_sum_of_same_parity(n, k))
