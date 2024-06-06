

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = []
    for i in range(n):
        temp = []
        for j in range(1,k+1):
            temp.append(str(j))
        ans.append(' '.join(temp[0:a[i]]))
    print('YES')
    for i in range(n):
        print(ans[i])
if __name__ == '__main__':
    main()
