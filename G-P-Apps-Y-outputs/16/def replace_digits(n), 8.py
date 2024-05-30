
def replace_digits(n):
    return int(str(n).replace('1', 'x').replace('9', '1').replace('x', '9'))

n = int(input())
print(replace_digits(n))
```
