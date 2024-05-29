
def count_special_numbers(n, k):
    MOD = 10**9 + 7

    def count_set_bits(x):
        count = 0
        while x > 0:
            count += 1
            x &= x - 1
        return count

    def is_special_num(num):
        operations = 0
        while num != 1:
            num = count_set_bits(num)
            operations += 1
            if operations > k:
                return False
        return operations == k

    count = 0
    for i in range(1, int(n, 2) + 1):
        if is_special_num(i):
            count = (count + 1) % MOD

    return count


n = input().strip()
k = int(input().strip())
print(count_special_numbers(n, k))
```
