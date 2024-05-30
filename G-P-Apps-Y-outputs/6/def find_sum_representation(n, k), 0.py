
def find_sum_representation(n, k):
    if n % 2 != k % 2:
        return "NO"

    if k > n:
        return "NO"

    if k == 1:
        return "YES\n{}".format(n)

    if n < k * k:
        return "NO"

    val = n // k
    ans = [str(val)] * k
    return "YES\n{}".format(" ".join(ans))

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n, k = map(int, input().split())
    result = find_sum_representation(n, k)
    print(result)
