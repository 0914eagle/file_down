
def solve(k, n1, n2, n3, t1, t2, t3):
    washers = [t1] * n1
    dryers = [t2] * n2
    folders = [t3] * n3
    laundry = []
    for i in range(k):
        laundry.append([t1, t2, t3])
    laundry.sort(key=lambda x: x[0])
    time = 0
    for piece in laundry:
        wash_time, dry_time, fold_time = piece
        wash_time += time
        dry_time += wash_time
        fold_time += dry_time
        time = fold_time
        washers.append(wash_time)
        dryers.append(dry_time)
        folders.append(fold_time)
    return time


k, n1, n2, n3, t1, t2, t3 = map(int, input().split())
print(solve(k, n1, n2, n3, t1, t2, t3))

