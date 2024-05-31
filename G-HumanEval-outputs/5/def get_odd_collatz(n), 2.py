
def get_odd_collatz(n):
    def collatz_sequence(num):
        sequence = [num]
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            sequence.append(num)
        return sequence

    collatz_numbers = collatz_sequence(n)
    return sorted([num for num in collatz_numbers if num % 2 != 0])

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
```
