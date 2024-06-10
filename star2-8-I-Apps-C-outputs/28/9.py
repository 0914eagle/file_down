

def earliest_time(S):
    n = len(S)
    time = 0
    for i in range(n):
        if S[i] == '1':
            time = max(time, i)
    return time

S = input()
print(earliest_time(S))


