
def get_odd_collatz(n):
    def collatz(num):
        sequence = [num]
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
            sequence.append(num)
        return sequence
    return sorted([i for i in collatz(n) if i % 2 != 0])

# Test the function with get_odd_collatz(5)
print(get_odd_collatz(5))  # Output: [1, 5]
```
