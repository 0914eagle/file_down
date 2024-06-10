
def solve(n, k, s):
    count = [0, 0, 0] # count[i] is the number of i-th color in s
    for c in s:
        count[ord(c) - ord('R')] += 1
    
    res = float('inf')
    for i in range(3): # try to make the i-th color as the first color of the substring
        first = i # the first color of the substring
        total = count[first] # the total number of first color in s
        for j in range(k):
            if (first + j) % 3 == 0:
                total -= count[0]
            elif (first + j) % 3 == 1:
                total -= count[1]
            else:
                total -= count[2]
        
        res = min(res, k - total)
        
    return res

def main():
    q = int(input())
    
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        
        print(solve(n, k, s))
        
main()

