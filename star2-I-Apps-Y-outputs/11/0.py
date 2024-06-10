
def next_permutation(num):
    num = list(str(num))
    i = len(num) - 1
    while i > 0:
        if num[i - 1] < num[i]:
            break
        i -= 1
    if i == 0:
        return 0
    j = len(num) - 1
    while num[j] <= num[i - 1]:
        j -= 1
    num[i - 1], num[j] = num[j], num[i - 1]
    num[i:] = num[len(num) - 1:i - 1:-1]
    return int(''.join(num))

x = int(input())
print(next_permutation(x))

