
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    def fibonacci(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

    count = 0
    num = 2
    while count < n:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            count += 1
        num += 1

    return fib_num

print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
