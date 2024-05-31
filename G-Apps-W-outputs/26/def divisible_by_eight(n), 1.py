
def divisible_by_eight(n):
    n_str = str(n)

    if len(n_str) <= 2 and int(n_str) % 8 == 0:
        return True, n_str

    for i in range(len(n_str)):
        for j in range(i + 1, len(n_str)):
            for k in range(j + 1, len(n_str)):
                num = int(n_str[i] + n_str[j] + n_str[k])
                if num % 8 == 0:
                    return True, str(num)

    return False, ""

n = int(input().strip())
possible, result = divisible_by_eight(n)

if possible:
    print("YES")
    print(result)
else:
    print("NO")
