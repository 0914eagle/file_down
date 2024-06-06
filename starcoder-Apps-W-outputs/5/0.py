
def solution(M, arr):
    if M == 0:
        for i in range(1, len(arr)+1):
            print(i)
    else:
        arr = arr.split('\n')
        dict_ = {}
        for i in arr:
            i = i.split(' ')
            i = [int(x) for x in i]
            if i[0] not in dict_:
                dict_[i[0]] = [i[1]]
            else:
                dict_[i[0]].append(i[1])
            if i[1] not in dict_:
                dict_[i[1]] = [i[0]]
            else:
                dict_[i[1]].append(i[0])
        not_in = []
        for i in dict_:
            if 1 not in dict_[i]:
                not_in.append(i)
        if len(not_in) != 0:
            for i in not_in:
                print(i)
        else:
            print("Connected")

T = input()
M = int(input())
arr = ""
for i in range(M):
    arr += input() + '\n'
solution(M, arr)
