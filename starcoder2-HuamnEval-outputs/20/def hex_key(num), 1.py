
def hex_key(num):
    primes = [2, 3, 5, 7, 11, 13]
    count = 0
    for i in num:
        if int(i, 16) in primes:
            count += 1
    return count
 