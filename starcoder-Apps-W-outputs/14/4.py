
n,m = [int(i) for i in input().split()]
students = []
for i in range(n):
    students.append(input())
scores = [int(i) for i in input().split()]
max_score = 0
for i in range(m):
    answer = ''
    for j in range(n):
        answer += students[j][i]
    count = {}
    for k in answer:
        if k not in count.keys():
            count[k] = 1
        else:
            count[k] += 1
    max_count = 0
    max_answer = ''
    for key,value in count.items():
        if value > max_count:
            max_count = value
            max_answer = key
    max_score += max_count * scores[i]
print(max_score)
