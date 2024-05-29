
def get_odd_collatz(n):
    def collatz(num):
        collatz_seq = [num]
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            collatz_seq.append(num)
        return collatz_seq

    collatz_list = collatz(n)
    odd_numbers = set(i for i in collatz_list if i % 2 != 0)
    return sorted(odd_numbers)

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
```
