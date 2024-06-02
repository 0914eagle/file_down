
def find_numbers(n, k):
    if n % 2 == 0:
        if k % 2 == 0:
            return "YES\n" + " ".join([str(n // k)] * k)
        else:
            if n < k:
                return "NO"
            else:
                return "YES\n" + " ".join([str(1)] * (k - 1)) + " " + str(n - (k - 1))
    else:
        if k % 2 == 0:
            return "NO"
        else:
            return "YES\n" + " ".join([str(1)] * (k - 1)) + " " + str(n - (k - 1))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_numbers(n, k))
