
t = int(input())

for _ in range(t):
    n = int(input())
    skills = list(map(int, input().split()))

    unique_skills = set()
    count_skills = {}
    for skill in skills:
        unique_skills.add(skill)
        if skill in count_skills:
            count_skills[skill] += 1
        else:
            count_skills[skill] = 1

    max_size = min(len(unique_skills), max(count_skills.values()))

    print(max_size)
``` 
