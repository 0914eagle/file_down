
def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1

    return primes if n != 0 else []

# Test cases
print(count_up_to(5))  # [2, 3]
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(0))  # []
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # []
print(count_up_to(18))  # [2, 3, 5, 7, 11, 13, 17]
