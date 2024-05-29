
def get_odd_collatz(n):
    def collatz_sequence(num):
        seq = [num]
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = 3*num + 1
            seq.append(num)
        return seq
    
    all_numbers = set()
    for i in range(1, n + 1):
        all_numbers.update(collatz_sequence(i))
    
    odd_numbers = sorted(list(filter(lambda x: x % 2 != 0, all_numbers)))
    return odd_numbers
