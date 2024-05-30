
def count_good_pairs(n, a, b):
    pairs = 0

    a_sum = []
    b_sum = []

    for i in range(n):
        a_sum.append(a[i] + b[i])
        b_sum.append(b[i] + a[i])

    a_sum.sort()
    b_sum.sort()

    for i in range(n):
        pairs += n - (len(list(filter(lambda x: x <= a_sum[i], b_sum))) + 1)

    return pairs // 2

# Input reading
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Call the function and print the output
print(count_good_pairs(n, a, b))
```
