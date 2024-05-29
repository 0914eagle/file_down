
def fizz_buzz(n: int):
    count = 0
    for num in range(n):
        if num % 11 == 0 or num % 13 == 0:
            count += str(num).count('7')
    return count

print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
