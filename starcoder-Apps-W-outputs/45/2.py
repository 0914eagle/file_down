
def solution():
    data = list(input())
    data1 = list(input())
    sum_ = 0
    n = len(data)
    for i in range(len(data1)):
        if data1[i] != '?':
            if data[i] == data1[i]:
                sum_ = sum_ + 1
    print(sum_/n)
solution()
