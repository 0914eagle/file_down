
from math import gcd

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    max_num = 0
    
    for i in range(n):
        is_valid = True
        
        for j in range(i):
            if gcd(a[j], a[i]) > 1:
                is_valid = False
        
        if is_valid:
            max_num = max(max_num, i + 1)
        
    print(max_num)
    
main()

