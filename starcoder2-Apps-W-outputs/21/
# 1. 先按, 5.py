
# 1. 先按照开始时间排序
# 2. 然后从前往后遍历，如果当前开始时间大于上一个结束时间，则说明上一个结束时间可以被覆盖
# 3. 然后将当前结束时间赋值给上一个结束时间，继续遍历

n, m = map(int, input().split())

workstations = []
for i in range(n):
    a, s = map(int, input().split())
    workstations.append((a, a + s))

workstations.sort(key=lambda x: x[0])

last_end = 0
count = 0
for start, end in workstations:
    if start >= last_end:
        count += 1
        last_end = end

print(count)
