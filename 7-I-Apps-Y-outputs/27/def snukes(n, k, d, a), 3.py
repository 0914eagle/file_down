
def snukes(n, k, d, a):
    # Write your code here
    count = 0
    for i in range(k):
        for j in range(d[i]):
            if a[i][j] == 1:
                count += 1
    return n - count

if __name__ == '__main__':
    n, k = map(int, input().split())
    d = [int(x) for x in input().split()]
    a = []
    for i in range(k):
        a.append([int(x) for x in input().split()])
    print(snukes(n, k, d, a))

