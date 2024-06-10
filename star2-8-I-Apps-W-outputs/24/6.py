
k, n1, n2, n3, t1, t2, t3 = map(int, input().split())
wash = [0] * n1
dry = [0] * n2
fold = [0] * n3
for _ in range(k):
    min_time = min(wash[i] + t1 for i in range(n1))
    min_idx = wash.index(min_time)
    wash[min_idx] = min_time
    min_time = min(dry[i] + t2 for i in range(n2))
    min_idx = dry.index(min_time)
    dry[min_idx] = max(min_time, wash[min_idx])
    min_time = min(fold[i] + t3 for i in range(n3))
    min_idx = fold.index(min_time)
    fold[min_idx] = max(min_time, dry[min_idx])
print(fold[-1])

