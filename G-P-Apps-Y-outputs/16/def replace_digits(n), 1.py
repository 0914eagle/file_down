
def replace_digits(n):
    n_str = str(n)
    replaced_str = n_str.replace('1', 'x').replace('9', '1').replace('x', '9')
    return int(replaced_str)

n = int(input())
print(replace_digits(n))
```
