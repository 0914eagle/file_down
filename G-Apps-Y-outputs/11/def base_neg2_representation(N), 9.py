
def base_neg2_representation(N):
    if N == 0:
        return '0'

    res = ''
    while N != 0:
        remainder = N % (-2)
        N = N // (-2)
        if remainder < 0:
            remainder += 2
            N += 1
        res = str(remainder) + res

    return res

N = int(input())
print(base_neg2_representation(N))
