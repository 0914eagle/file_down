
def count_valid_ways(A, B):
    n = len(A)
    diff_count = 0
    for i in range(n):
        if A[i] != B[i]:
            diff_count += 1

    if diff_count % 2 != 0:
        return 0

    diff_count //= 2

    start = 0
    end = 0
    diff_so_far = 0
    result = 1

    while end < n:
        while diff_so_far < diff_count:
            if A[end] != B[end]:
                diff_so_far += 1
            end += 1

        while diff_so_far >= diff_count:
            if A[start] != B[start]:
                diff_so_far -= 1
            start += 1

        result += end - start

    return result

# Input
A = input().strip()
B = input().strip()

# Output
print(count_valid_ways(A, B))
