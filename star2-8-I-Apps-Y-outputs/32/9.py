
n, k = [int(x) for x in input().split()]
skills = [int(x) for x in input().split()]
quarrels = [tuple(sorted([int(x) for x in input().split()])) for _ in range(k)]
quarrels = set(quarrels)
mentors = [0] * n
sorted_skills = sorted(enumerate(skills), key=lambda x: x[1])
for i, skill in sorted_skills:
    can_be_mentor = 0
    for j, other_skill in sorted_skills:
        if skill < other_skill and (i, j) not in quarrels:
            can_be_mentor += 1
    mentors[i] = can_be_mentor
for m in mentors:
    print(m, end=" ")

