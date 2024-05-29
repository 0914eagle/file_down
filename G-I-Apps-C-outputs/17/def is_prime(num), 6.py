
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_divisor(arr):
    max_score = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub_arr = arr[i:j+1]
            min_num = min(sub_arr)
            
            for num in range(min_num, 0, -1):
                if is_prime(num):
                    if all(elem % num == 0 for elem in sub_arr):
                        max_score = max(max_score, num)
                        break
                    
    return max_score

def max_score_partition(n, k, v):
    max_score = 0
    for i in range(1, len(v) - k + 2):
        score = largest_prime_divisor(v[:i]) + max_score_partition(n - i, k - 1, v[i:])
        max_score = max(max_score, score)
    return max_score

n, k = map(int, input().split())
v = list(map(int, input().split()))

result = max_score_partition(n, k, v)
print(result)
```
