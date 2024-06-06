
# -*- coding: utf-8 -*-


n, m = map(int, input().split())
A = []
score = 0
for i in range(n):
    A.append(input())
    
score_lst = list(map(int, input().split()))

def max_score(lst, score_lst):
    max_score = 0
    for j in range(len(lst)):
        max_score += score_lst[lst.index(max(lst))]
        lst[lst.index(max(lst))] = 0
    return max_score

for j in range(m):
    lst = [0] * n
    for i in range(n):
        if A[i][j] == 'A':
            lst[i] += score_lst[0]
        elif A[i][j] == 'B':
            lst[i] += score_lst[1]
        elif A[i][j] == 'C':
            lst[i] += score_lst[2]
        elif A[i][j] == 'D':
            lst[i] += score_lst[3]
        elif A[i][j] == 'E':
            lst[i] += score_lst[4]
    score += max_score(lst, score_lst)
    
print(score)
