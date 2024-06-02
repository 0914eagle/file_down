
def find_max_divisible_by_2(N):
    max_divisible = 0
    max_num = 0
    for num in range(1, N+1):
        count = 0
        while num % 2 == 0:
            count += 1
            num //= 2
        if count > max_divisible:
            max_divisible = count
            max_num = num
    return max_num

N = int(input())
print(find_max_divisible_by_2(N))
