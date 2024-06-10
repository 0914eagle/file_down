
n, k = map(int, input().split())
skills = list(map(int, input().split()))
quarrels = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
quarrels_set = set(quarrels)
sorted_skills = sorted(enumerate(skills), key=lambda x: x[1])
can_be_mentor = [0] * n
for i, skill in sorted_skills:
    can_be_mentor_num = 0
    for j, other_skill in sorted_skills:
        if i == j:
            break
        if skill > other_skill and (i, j) not in quarrels_set:
            can_be_mentor_num += 1
    can_be_mentor[i] = can_be_mentor_num
print(" ".join(map(str, can_be_mentor)))

