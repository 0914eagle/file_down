
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def any_int(x, y, z):
    if is_prime(x) and is_prime(y) and is_prime(z):
        return True
    elif is_odd(x) and is_odd(y) and is_odd(z):
        return True
    else:
        return False
 