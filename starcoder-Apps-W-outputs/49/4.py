

n = int(input())
for _ in range(n):
    a = input()
    print(a[0], end='')
    for i in range(1,len(a)):
        print(chr(ord('a')+(i%26)), end='')
    print()

