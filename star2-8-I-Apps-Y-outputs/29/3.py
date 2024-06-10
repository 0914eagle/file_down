
def solution(n, a):
    count = 0
    for i in range(n):
        if a[i] >= i + 1:
            count += 1
        else:
            break
    
    return count


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    
    print(solution(n, a))

