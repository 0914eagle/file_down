
def get_odd_collatz(n):
    def collatz_sequence(num):
        seq = [num]
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            seq.append(num)
        return seq

    collatz_seq = collatz_sequence(n)
    odd_numbers = sorted(set(filter(lambda x: x % 2 != 0, collatz_seq)))
    return odd_numbers

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
```
