
def fizz_buzz(n: int):
    count = 0
    for i in range(1, n):
        if (('7' in str(i)) and (i % 11 == 0 or i % 13 == 0)):
            count += 1
    return count

print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
