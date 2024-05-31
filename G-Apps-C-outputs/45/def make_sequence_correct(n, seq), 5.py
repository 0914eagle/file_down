
def make_sequence_correct(n, seq):
    opens = 0
    unpaired_closes = 0
    nanoseconds = 0
    
    for char in seq:
        if char == '(':
            opens += 1
        else:
            if opens == 0:
                unpaired_closes += 1
            else:
                opens -= 1
    
    if opens % 2 != 0:
        return -1
    
    nanoseconds += unpaired_closes // 2
    opens += unpaired_closes // 2
    
    nanoseconds += opens
    return nanoseconds

n = int(input())
seq = input().strip()

result = make_sequence_correct(n, seq)
print(result)
