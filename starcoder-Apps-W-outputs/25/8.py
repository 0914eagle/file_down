
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

s,b = map(int,input().split())

a = list(map(int,input().split()))

for i in range(b):
    d,g = map(int,input().split())

    for j in a:
        if j<=d:
            print(g,end=" ")
            break
        else:
            print(0,end=" ")
    print()
