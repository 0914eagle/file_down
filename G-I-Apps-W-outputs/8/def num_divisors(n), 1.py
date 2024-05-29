
import math

def num_divisors(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                divisors += 1
            else:
                divisors += 2
    return divisors

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

def shortest_subsequence_length(a, n):
    current_subsequence = set()
    for num in a:
        if is_perfect_square(num):
            return 1
        new_subsequence = set()
        for sub_num in current_subsequence:
            new_num = sub_num * num
            if is_perfect_square(new_num):
                return 2
            new_subsequence.add(new_num)
        new_subsequence.add(num)
        current_subsequence = current_subsequence.union(new_subsequence)
    return -1

n = int(input())
a = list(map(int, input().split()))

print(shortest_subsequence_length(a, n))
```
