
import sys
def valid_num(num,valid_nums):
    str_num = str(num)
    for i in str_num:
        if i in valid_nums:
            continue
        else:
            return False
    return True

def multiple(X,A,B):
    res = 0
    for i in range(A,B+1):
        if valid_num(i,X) == True and i % int(X) == 0:
            res += 1
    return res

def main():
    X,A,B = sys.stdin.readline().split()
    valid_nums = sys.stdin.readline().strip('\n')
    print(multiple(X,int(A),int(B)))

if __name__ == '__main__':
    main()
