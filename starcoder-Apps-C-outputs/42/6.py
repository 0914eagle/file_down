
def main():
    n = int(input())
    lis = [input().split() for i in range(n)]
    ans = []
    for i in range(n):
        for j in range(n):
            if i != j:
                ans.append(int((int(lis[i][j])**2-int(lis[j][i])**2)**0.5))
            else:
                ans.append(0)
    for i in range(n):
        print(ans[i], end = ' ')
if __name__ == '__main__':
    main()
