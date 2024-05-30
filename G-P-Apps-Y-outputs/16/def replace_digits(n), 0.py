
def replace_digits(n):
    n = str(n)
    n = n.replace('1', 'x').replace('9', '1').replace('x', '9')
    return int(n)

n = int(input())
result = replace_digits(n)
print(result)
```
