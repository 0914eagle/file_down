
k, n1, n2, n3, t1, t2, t3 = map(int, input().split())

wash_queue = [0] * n1
dry_queue = [0] * n2
fold_queue = [0] * n3

for i in range(k):
  wash_queue[i % n1] += t1
  dry_queue[i % n2] = max(dry_queue[i % n2], wash_queue[i % n1]) + t2
  fold_queue[i % n3] = max(fold_queue[i % n3], dry_queue[i % n2]) + t3

print(max(fold_queue))

