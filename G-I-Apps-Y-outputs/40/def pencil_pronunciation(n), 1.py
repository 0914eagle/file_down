
def pencil_pronunciation(n):
    last_digit = n % 10
    if last_digit in [2, 4, 5, 7, 9]:
        return "hon"
    elif last_digit in [0, 1, 6, 8]:
        return "pon"
    else:
        return "bon"

N = int(input())
print(pencil_pronunciation(N))
