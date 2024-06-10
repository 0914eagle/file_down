
n = int(input())

max_len = 0
max_lucky = 0
for i in range(7 ** n, 8 ** n + 1):
    if '7' not in str(i) or '8' not in str(i):
        continue
    
    if len(str(i)) > max_len:
        max_len = len(str(i))
        max_lucky = 1
    elif len(str(i)) == max_len:
        max_lucky += 1

print(max_lucky)

