
import math

def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num

def find_shortest_subsequence(n, arr):
    min_length = n
    for i in range(1, 1 << n):
        subsequence = [arr[j] for j in range(n) if (i & (1 << j))]
        product = 1
        for num in subsequence:
            product *= num
        if is_perfect_square(product):
            min_length = min(min_length, len(subsequence))
    return min_length if min_length != n else -1

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Find and output the length of the shortest subsequence
print(find_shortest_subsequence(n, arr))
