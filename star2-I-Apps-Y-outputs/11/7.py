
def find_next_number(num):
    num_str = str(num)
    digits = list(num_str)
    n = len(digits)

    i = n - 1
    while i > 0:
        if digits[i] > digits[i - 1]:
            break
        i -= 1

    if i == 0:
        return 0

    x = digits[i - 1]
    smallest = i
    for j in range(i + 1, n):
        if digits[j] > x and digits[j] < digits[smallest]:
            smallest = j

    digits[i - 1], digits[smallest] = digits[smallest], digits[i - 1]
    digits[i:] = reversed(digits[i:])

    return int("".join(digits))

num = int(input())
next_number = find_next_number(num)
print(next_number)

