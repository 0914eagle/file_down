
def main():
    N,M = map(int,input().split())
    P = list(map(int,input().split()))
    R = list(map(int,input().split()))
    time = [0]*M
    event = []
    for i in range(N):
        C,T = map(int,input().split())
        event.append([T,C])
    event.sort(reverse=True)
    res = 0
    for i in range(N):
        T,C = event[i][0],event[i][1]
        if time[C-1]<=T:
            time[C-1] = T+R[C-1]+P[C-1]
            res += 1
    print(res)
if __name__ == '__main__':
    main()
