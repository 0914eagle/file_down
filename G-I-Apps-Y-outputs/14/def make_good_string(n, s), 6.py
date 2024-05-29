
def make_good_string(n, s):
    new_s = []
    delete_count = 0
    for i in range(n):
        if i % 2 == 0 or s[i] != s[i - 1]:
            new_s.append(s[i])
        else:
            delete_count += 1
    return delete_count, "".join(new_s)

# Input
n = int(input())
s = input()

# Solve the problem
delete_count, new_s = make_good_string(n, s)

# Output
print(delete_count)
print(new_s)
```  
