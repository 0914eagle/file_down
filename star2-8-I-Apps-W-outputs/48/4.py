
def isPerfect(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum == 10

def findPerfect(k):
    perfectList = []
    n = 1
    while len(perfectList) < k:
        if isPerfect(n):
            perfectList.append(n)
        n += 1
    return perfectList[-1]

k = int(input())
print(findPerfect(k))

