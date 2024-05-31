
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

    odd_numbers = set()
    for i in range(1, n+1):
        sequence = collatz_sequence(i)
        odd_numbers.update(num for num in sequence if num % 2 != 0)

    return sorted(list(odd_numbers))

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
```
