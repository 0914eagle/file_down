
# 解题思路
# 先对所有人按到达时间排序，然后从第一个人开始，如果当前人到达时间大于上一个人离开时间，则说明上一个人离开后没有人使用，
# 则可以直接给当前人分配，如果当前人到达时间小于上一个人离开时间，则说明上一个人离开后有人使用，则需要给上一个人分配，
# 然后再给当前人分配，所以需要给上一个人分配两次，然后将当前人离开时间赋值给上一个人离开时间，继续遍历下一个人，
# 直到遍历完所有人，然后输出结果。

n,m = map(int,input().split())

# 先对所有人按到达时间排序
people = []
for i in range(n):
    a,s = map(int,input().split())
    people.append([a,s])
people.sort(key=lambda x:x[0])

# 记录上一个人离开时间
last_leave_time = 0
# 记录总共需要分配的次数
count = 0
for i in range(n):
    # 如果当前人到达时间大于上一个人离开时间，则说明上一个人离开后没有人使用，则可以直接给当前人分配
    if people[i][0] > last_leave_time:
        count += 1
        last_leave_time = people[i][0] + people[i][1]
    # 如果当前人到达时间小于上一个人离开时间，则说明上一个人离开后有人使用，则需要给上一个人分配，
    # 然后再给当前人分配，所以需要给上一个人分配两次
    else:
        count += 2
        last_leave_time = people[i][0] + people[i][1]
print(count)
