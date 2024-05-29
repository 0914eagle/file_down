
def get_odd_collatz(n):
    def collatz_sequence(num):
        seq = [num]
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
            seq.append(num)
        return seq
    
    collatz_list = collatz_sequence(n)
    return sorted(set(filter(lambda x: x % 2 != 0, collatz_list)))

# Test the function with example
print(get_odd_collatz(5))  # Output: [1, 5]
```
