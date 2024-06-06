
N, M = list(map(int, input().split()))
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = []
for _ in range(N):
    line = input().split()
    start_date = int(line[1])*100+int(line[0])
    end_date = int(line[3])*100+int(line[2])
    event_num = line[4:]
    for i in range(len(event_num)):
        if event_num[i] != '0':
            result.append([i, end_date-start_date+1])
if len(result) != M:
    print(-1)
else:
    for _ in range(len(result)):
        for i in range(1, M):
            if result[i][1] != result[i-1][1]:
                print(-1)
                exit(0)
    print(result[0][1])
