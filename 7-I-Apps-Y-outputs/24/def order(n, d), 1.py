
def order(n, d):
    # Write your code here
    d.insert(0, 0)
    d.append(0)
    for i in range(1, n):
        if d[i] == 0:
            d[i] = d[i-1] + 1
        elif d[i] > d[i-1]:
            d[i] = d[i-1] + 1
    return d

if __name__ == '__main__':
    n = int(input())
    d = list(map(int, input().split()))
    print(*order(n, d))

