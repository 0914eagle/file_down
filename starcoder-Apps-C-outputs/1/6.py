
def main():
    L,R = map(int,input().split())
    res = [0]*10
    for i in range(L,R+1):
        for j in str(i):
            if j != '0':
                res[int(j)] += 1
    print(' '.join(map(str,res)))

if __name__ == "__main__":
    main()
