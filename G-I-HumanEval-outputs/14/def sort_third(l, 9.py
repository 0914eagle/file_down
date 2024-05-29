
def sort_third(l: list):
    non_divisible_by_three = [l[i] for i in range(len(l)) if i % 3 != 0]
    divisible_by_three = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    
    result = []
    ndx = 0
    dd = 0
    for i in range(len(l)):
        if i % 3 != 0:
            result.append(non_divisible_by_three[ndx])
            ndx += 1
        else:
            result.append(divisible_by_three[dd])
            dd += 1
            
    return result


# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
```
