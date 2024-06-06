
# Note: this code is not entirely correct yet. It is a start.
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    if a[i] > b[i]:
        print("The number of bottles can't be less than the number of the soda")
        break

counter = 0
for i in range(n):
    counter += (a[i] // b[i])

print(counter)

time = 0
for i in range(n):
    time += a[i] // b[i]

print(time)
