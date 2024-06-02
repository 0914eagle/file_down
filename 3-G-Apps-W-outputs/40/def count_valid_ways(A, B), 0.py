
def count_valid_ways(A, B):
    n = len(A)
    diff_count = 0
    for i in range(n):
        if A[i] != B[i]:
            diff_count += 1

    if diff_count % 2 != 0:
        return 0

    diff_count //= 2
    diff_count_a = 0
    diff_count_b = 0
    valid_ways = 0

    for i in range(n):
        if A[i] != B[i]:
            if diff_count_a < diff_count:
                diff_count_a += 1
            else:
                diff_count_b += 1
        else:
            if diff_count_a > 0:
                valid_ways += 1
                diff_count_a -= 1
            elif diff_count_b > 0:
                valid_ways += 1
                diff_count_b -= 1

    return valid_ways

# Input
A = input().strip()
B = input().strip()

# Output
print(count_valid_ways(A, B))
