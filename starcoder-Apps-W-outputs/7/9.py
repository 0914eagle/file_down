
n, m, k = map(int, input().split())

print(2*k + n + m - 2)

for i in range(1, k+1):
    print(f"(1,1) ({i+1},1)")
for i in range(1, n):
    print(f"(1,1) (1,{i+1})")
