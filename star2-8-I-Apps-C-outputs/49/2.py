
n, l = list(map(int, input().split()))
a = list(map(int, input().split()))
c = list(map(int, input().split()))

farmers = list(zip(a, c))
farmers.sort(key=lambda x: x[1] / x[0])

first_sum = 0
second_sum = 0
for i in range(n):
    if i < l:
        first_sum += farmers[i][0]
    else:
        second_sum += farmers[i][0]

print(farmers[l - 1][1] / first_sum * farmers[n - 1][1] / second_sum)

