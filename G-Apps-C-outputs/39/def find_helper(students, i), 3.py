
def find_helper(students, i):
    max_knowledge = float('-inf')
    min_diff_knowledge = float('inf')
    min_diff_understanding = float('inf')
    helper = "NE"
    
    for j in range(i-1, -1, -1):
        if students[j][0] >= students[i][0] and students[j][1] >= students[i][1]:
            diff_knowledge = students[j][0] - students[i][0]
            diff_understanding = students[j][1] - students[i][1]
            
            if diff_knowledge < min_diff_knowledge or (diff_knowledge == min_diff_knowledge and diff_understanding < min_diff_understanding):
                min_diff_knowledge = diff_knowledge
                min_diff_understanding = diff_understanding
                max_knowledge = students[j][1]
                helper = j+1
    
    return helper

N = int(input())
students = []
for _ in range(N):
    query = input().split()
    if query[0] == "D":
        students.append((int(query[1]), int(query[2]))
    else:
        i = int(query[1]) - 1
        helper = find_helper(students, i)
        print(helper)

