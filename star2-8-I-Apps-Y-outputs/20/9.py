
N = int(input())
divisors = [0] * (N+1)
for i in range(1, N+1):
    n = i
    while n % 2 == 0:
        divisors[i] += 1
        n //= 2
max_divisors = max(divisors)
for i in range(1, N+1):
    if divisors[i] == max_divisors:
        print(i)
        break

