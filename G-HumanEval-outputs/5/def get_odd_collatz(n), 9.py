
def get_odd_collatz(n):
    def collatz(num):
        sequence = [num]
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            sequence.append(num)
        return sequence

    collatz_sequence = collatz(n)
    odd_numbers = sorted(set(filter(lambda x: x % 2 != 0, collatz_sequence)))

    return odd_numbers

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
```
