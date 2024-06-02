
def find_numbers(n, k):
    if n % 2 == 0:
        if k % 2 == 0:
            return "YES\n" + " ".join([str(n // k)] * k)
        else:
            if n >= k * 2:
                return "YES\n" + " ".join([str(2)] * (k - 1)) + " " + str(n - 2 * (k - 1))
            else:
                return "NO"
    else:
        if k % 2 == 1:
            return "YES\n" + " ".join([str(1)] * (k - 1)) + " " + str(n - (k - 1))
        else:
            return "NO"

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_numbers(n, k))
