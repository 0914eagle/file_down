
import sys

N = int(input())

C = []
S = []
F = []

for i in range(N):
    C.append(int(input()))
    S.append(int(input()))
    F.append(int(input()))


def find_time(i, N):
    if i == N - 1:
        return S[i]
    else:
        return S[i] + find_time(i + 1, N) + C[i]


def find_time_from_station(i, N):
    if i == N - 1:
        return S[i]
    else:
        return S[i] + find_time_from_station(i + 1, N) + C[i]


for i in range(N):
    print(find_time(i, N))


