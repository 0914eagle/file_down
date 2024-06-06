
n, m = map(int, input().split())
# 员工的id、工资、身高
employee_list = [0]
for _ in range(n):
    id, salary, height = map(int, input().split())
    employee_list.append([id, salary, height])

# 主管的id、主管的工资、主管的身高
boss_list = [0]

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if employee_list[i][1] < employee_list[j][1] and employee_list[i][2] <= employee_list[j][2]:
            boss_list.append(employee_list[j])
            break
    else:
        boss_list.append(employee_list[i])

# 查询的员工的id
for _ in range(m):
    employee_id = int(input())
    # 员工是谁的下属
    index = employee_list.index([employee_id, 0, 0])
    # 员工的主管是谁
    boss_index = boss_list.index(employee_list[index])
    print(boss_list[boss_index][0], end=' ')
    # 查询的员工的下属个数
    subordinates = 0
    for i in range(n + 1):
        # 这里找下属，和找主管是同一个操作
        # 找下属，工资比查询的员工的工资高，身高比查询的员工的身高高
        if employee_list[i][1] > employee_list[index][1] and employee_list[i][2] > employee_list[index][2]:
            # 主管是谁
            boss_index = boss_list.index(employee_list[i])
            if boss_list[boss_index][0] == employee_list[index][0]:
                subordinates += 1
    print(subordinates)
