
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n):
    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return (even_palindromes, odd_palindromes)

# Test cases
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
```
