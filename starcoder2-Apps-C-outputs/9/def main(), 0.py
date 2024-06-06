
def main():
    n = int(input())
    a = []
    for i in range(1,n):
        for j in range(i+1,n):
            if i < j and (str(i) + str(j) + str(i+j)).replace("0","") == str(i+j):
                a.append([i,j])
    print(len(a))
    for i in a:
        print(i[0],i[1])
if __name__ == '__main__':
    main()
