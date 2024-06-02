
def max_divisible_by_2(N):
    max_divisible = 0
    max_num = 0
    for i in range(1, N+1):
        count = 0
        num = i
        while num % 2 == 0:
            count += 1
            num //= 2
        if count > max_divisible:
            max_divisible = count
            max_num = i
    return max_num

# Read input from Standard Input
N = int(input())

# Call the function and print the result
print(max_divisible_by_2(N))
