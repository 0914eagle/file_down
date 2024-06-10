
N, L = map(int, input().split())
apple = []
for i in range(N):
  apple.append(L + i)
apple.sort(reverse=True)
apple.pop(0)
print(sum(apple))

