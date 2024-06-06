
n, m, k = map(int, input().split())
print(n*m+1)
for i in range(1, k+1):
    print(f"(1,1) ({i+1},1)")
