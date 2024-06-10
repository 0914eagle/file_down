
t = int(input())
for _ in range(t):
    s = input()
    if s.find('010') == -1 and s.find('101') == -1:
        print(0)
    else:
        print(1)

