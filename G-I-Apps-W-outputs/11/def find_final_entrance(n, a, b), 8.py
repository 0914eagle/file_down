
def find_final_entrance(n, a, b):
    final_entrance = a + b % n
    if final_entrance <= 0:
        return n + final_entrance
    elif final_entrance > n:
        return final_entrance - n
    else:
        return final_entrance

# Read input
n, a, b = map(int, input().split())
print(find_final_entrance(n, a, b))
```
