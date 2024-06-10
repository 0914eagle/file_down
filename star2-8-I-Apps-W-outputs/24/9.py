
k, n_1, n_2, n_3, t_1, t_2, t_3 = map(int, input().split())
wash_times = []
dry_times = []
fold_times = []
for i in range(k):
    wash_times.append(i * t_1)
    dry_times.append(wash_times[i] + t_2)
    fold_times.append(dry_times[i] + t_3)
min_time = max(fold_times)
print(min_time)

