
def prime_length(string):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    length = len(string)
    return is_prime(length)

assert prime_length('Hello') == True
assert prime_length('abcdcba') == True
assert prime_length('kittens') == True
assert prime_length('orange') == False
