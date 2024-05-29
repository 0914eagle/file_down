
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n):
    count_even = 0
    count_odd = 0

    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

    return (count_even, count_odd)

# Test examples
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
```
