
def find_sequences(n, sequence):
    inc_seq = []
    dec_seq = []
    
    for i in range(n):
        if not inc_seq or inc_seq[-1] < sequence[i]:
            inc_seq.append(sequence[i])
        elif not dec_seq or dec_seq[-1] > sequence[i]:
            dec_seq.append(sequence[i])
        else:
            print("NO")
            return
    
    print("YES")
    print(len(inc_seq))
    print(" ".join(map(str, inc_seq)))
    print(len(dec_seq))
    print(" ".join(map(str, dec_seq[::-1]))

# Input parsing
n = int(input())
sequence = list(map(int, raw_input().split()))

find_sequences(n, sequence)
```
