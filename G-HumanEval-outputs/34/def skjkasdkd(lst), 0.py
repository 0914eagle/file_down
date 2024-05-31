
def skjkasdkd(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def sum_digits(num):
        return sum(int(digit) for digit in str(num))

    primes = [num for num in lst if is_prime(num)]
    if not primes:
        return 0

    max_prime = max(primes)
    return sum_digits(max_prime)
