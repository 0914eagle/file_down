
def count_nums(arr):
    def get_digit_sum(num):
        num = abs(num)
        total = 0
        while num:
            total += num % 10
            num //= 10
        return total

    count = 0
    for num in arr:
        if get_digit_sum(num) > 0:
            count += 1
    return count

# Test cases
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)
```
