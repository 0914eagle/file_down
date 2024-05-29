
def find_initial_sequences(n, a):
    inc_seq = []
    dec_seq = []
    
    inc_flag = False
    dec_flag = False
    
    for num in a:
        if not inc_flag or inc_seq[-1] < num:
            inc_seq.append(num)
            inc_flag = True
        elif not dec_flag or dec_seq[-1] > num:
            dec_seq.append(num)
            dec_flag = True
        else:
            return "NO"
    
    print("YES")
    print(len(inc_seq))
    print(*inc_seq)
    print(len(dec_seq))
    print(*dec_seq[::-1])

# Reading input
n = int(input())
a = list(map(int, input().split()))

# Calling the function
find_initial_sequences(n, a)
```
