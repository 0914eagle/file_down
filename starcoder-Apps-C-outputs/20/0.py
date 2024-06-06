
# 自己用字典做的 超时
def func(list1):
    list2 = []
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i][0]==list1[j][0] and list1[i][-1]==list1[j][-1]:
                list2.append(list1[i]+list1[j])
    if len(list2)==0:
        return 0
    else:
        return max([len(x) for x in list2])

n = int(input())
list1 = []
for i in range(n):
    list1.append(input())
print(func(list1))
