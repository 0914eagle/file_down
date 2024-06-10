
k, n1, n2, n3, t1, t2, t3 = map(int, input().split())

wash_time = [0] * k
dry_time = [0] * k
fold_time = [0] * k

for i in range(k):
    if i < n1:
        wash_time[i] = t1
    else:
        wash_time[i] = t1 + max(wash_time[i - n1 : i])

for i in range(k):
    if i < n2:
        dry_time[i] = wash_time[i] + t2
    else:
        dry_time[i] = wash_time[i] + t2 + max(dry_time[i - n2 : i])

for i in range(k):
    if i < n3:
        fold_time[i] = dry_time[i] + t3
    else:
        fold_time[i] = dry_time[i] + t3 + max(fold_time[i - n3 : i])

print(fold_time[-1])

