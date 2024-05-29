
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def prime_length(string):
    length = len(string)
    return is_prime(length)

print(prime_length('Hello')) # Output: True
print(prime_length('abcdcba')) # Output: True
print(prime_length('kittens')) # Output: True
print(prime_length('orange')) # Output: False
