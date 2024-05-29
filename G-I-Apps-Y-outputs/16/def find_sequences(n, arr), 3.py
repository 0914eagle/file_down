
def find_sequences(n, arr):
    arr_sorted = sorted(arr)
    inc_seq = []
    dec_seq = []
    
    for num in arr_sorted:
        if num in set(inc_seq):
            dec_seq.append(num)
        else:
            inc_seq.append(num)
    
    if len(set(inc_seq)) + len(set(dec_seq)) != n:
        print("NO")
    else:
        print("YES")
        print(len(inc_seq))
        print(" ".join(map(str, inc_seq)))
        print(len(dec_seq))
        print(" ".join(map(str, dec_seq[::-1]))

# Input
n = int(input())
arr = list(map(int, input().split()))

# Call the function
find_sequences(n, arr)
```
