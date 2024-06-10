
[...]


n, m = map(int, input().split())
y = [0] * (m + 1) # y[i] is the minimum value of |y| among all the shopping malls that sell item i
for _ in range(n):
    x, y[t], t = map(int, input().split())
print(sum(y[i] for i in range(1, m + 1)))

