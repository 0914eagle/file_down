
def symmetric_difference():
    M = int(input())
    set_M = set(map(int, input().split()))
    
    N = int(input())
    set_N = set(map(int, input().split()))
    
    result = sorted(set_M.symmetric_difference(set_N))
    
    for num in result:
        print(num)

# Test the function
symmetric_difference()