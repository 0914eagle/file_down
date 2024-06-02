
def find_max_divisible_by_2(N):
    max_divisible = 0
    for i in range(1, N+1):
        count = 0
        num = i
        while num % 2 == 0:
            count += 1
            num //= 2
        if count > max_divisible:
            max_divisible = count
            result = i
    return result

N = int(input())
print(find_max_divisible_by_2(N))
