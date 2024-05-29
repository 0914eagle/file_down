
def find_maximum_number(n, a, mappings):
    modified = False
    result = ''
    
    for digit in a:
        mapped_digit = mappings[int(digit) - 1]
        if mapped_digit > digit and not modified:
            modified = True
            result += str(mapped_digit)
        else:
            result += str(digit)
    
    return result

# Input
n = int(input())
a = input()
mappings = list(map(int, input().split()))

# Output
print(find_maximum_number(n, a, mappings))
```
