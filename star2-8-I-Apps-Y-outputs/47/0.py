
n, p, k = map(int, input().split())
events = list(map(int, input().split()))
def time_to_speed(t):
    return (100 + p*t)/100
original_length = k
for i in range(n):
    original_length *= time_to_speed(i)
    original_length -= events[i]
print(original_length)


n = int(input())
c = 0
for k in range(1, n+1):
    for d in range(1, 11):
        if k % d == 0:
            c += 1
            break
print(c)

