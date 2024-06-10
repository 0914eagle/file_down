
def find_next_number(x):
    digits = list(str(x))
    n = len(digits)
    i = n - 1
    while i > 0:
        if digits[i - 1] < digits[i]:
            break
        i -= 1
    if i == 0:
        return 0
    j = n - 1
    while digits[j] <= digits[i - 1]:
        j -= 1
    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    digits[i:] = digits[n - 1:i - 1:-1]
    return int(''.join(digits))
x = int(input())
print(find_next_number(x))

