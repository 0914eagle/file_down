
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def ceil_div(x, y):
    return (x + y - 1) // y

def calc_time(order):
    time = 0
    for dish in order:
        if dish == 'A':
            time = ceil_div(time, 10) * 10 + A
        elif dish == 'B':
            time = ceil_div(time, 10) * 10 + B
        elif dish == 'C':
            time = ceil_div(time, 10) * 10 + C
        elif dish == 'D':
            time = ceil_div(time, 10) * 10 + D
        elif dish == 'E':
            time = ceil_div(time, 10) * 10 + E
    return time

order = 'ABCDE'
ans = float('inf')
for i in range(5):
    for j in range(5):
        if i == j:
            continue
        for k in range(5):
            if i == k or j == k:
                continue
            for l in range(5):
                if i == l or j == l or k == l:
                    continue
                for m in range(5):
                    if i == m or j == m or k == m or l == m:
                        continue
                    ans = min(ans, calc_time(order[i] + order[j] + order[k] + order[l] + order[m]))

print(ans)

