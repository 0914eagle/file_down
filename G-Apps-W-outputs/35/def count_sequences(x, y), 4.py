
def count_sequences(x, y):
    MOD = 10**9 + 7
    
    # Helper function to calculate the modular inverse
    def mod_inverse(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1
    
    # Helper function to calculate the number of positive divisors of a number
    def count_divisors(num):
        count = 0
        i = 1
        while i*i <= num:
            if num % i == 0:
                if num // i == i:
                    count += 1
                else:
                    count += 2
            i += 1
        return count
    
    # If y is not divisible by x, there are no suitable sequences
    if y % x != 0:
        return 0
    
    y_divisors = count_divisors(y // x)
    
    # Calculate the answer using the formula based on Euler's Totient function
    ans = pow(2, y_divisors - 1, MOD)
    
    return ans

# Input
x, y = map(int, input().split())

# Output
print(count_sequences(x, y))
