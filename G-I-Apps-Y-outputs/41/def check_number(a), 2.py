
def check_number(a):
    if a % 2 == 0 and a % 3 == 0 and a % 5 == 0:
        return 1
    else:
        return 0

a = int(input())
print(check_number(a))
```
