
import math
T = int(input())
for i in range(T):
    N = int(input())
    min_A = [0] * N
    min_B = [0] * N
    min_C = [0] * N
    for j in range(N):
        min_A[j], min_B[j], min_C[j] = map(int, input().split())
    max_people = 0
    for j in range(N):
        people = 0
        for k in range(N):
            if j != k and min_A[j] <= min_A[k] and min_B[j] <= min_B[k] and min_C[j] <= min_C[k]:
                people += 1
        max_people = max(max_people, people)
    print("Case #{}: {}".format(i+1, max_people))

