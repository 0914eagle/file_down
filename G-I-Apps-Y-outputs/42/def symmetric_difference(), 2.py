
def symmetric_difference():
    M = int(input())
    set_M = set(map(int, input().split()))
    
    N = int(input())
    set_N = set(map(int, input().split()))
    
    result = sorted(set_M.symmetric_difference(set_N))
    
    for val in result:
        print(val)

symmetric_difference()
```

This function takes input for two sets of integers `M` and `N`, finds their symmetric difference, sorts the result in ascending order, and prints the integers one per line.

Feel free to ask if you have any questions or need further assistance! 
```

