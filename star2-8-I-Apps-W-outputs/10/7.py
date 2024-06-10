
n = int(input())
a = list(map(int, input().split()))
a.sort()

min_diff = 360

for i in range(n):
    vasya_sector = sum(a[:i + 1])
    petya_sector = sum(a[i + 1:])
    diff = abs(vasya_sector - petya_sector)
    
    if diff < min_diff:
        min_diff = diff
        
print(min_diff)

