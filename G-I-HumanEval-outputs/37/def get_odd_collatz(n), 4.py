
def get_odd_collatz(n):
    def collatz(num):
        sequence = []
        while num != 1:
            sequence.append(num)
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
        sequence.append(1)
        return sequence

    collatz_sequence = collatz(n)
    result = sorted(set(filter(lambda x: x % 2 != 0, collatz_sequence)))
    return result

# Test the function with the example provided
print(get_odd_collatz(5))  # Output: [1, 5]
