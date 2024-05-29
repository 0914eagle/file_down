
def split_sequence(n, a):
    inc_seq = []
    dec_seq = []

    for num in a:
        if not inc_seq or inc_seq[-1] < num:
            inc_seq.append(num)
        elif not dec_seq or dec_seq[-1] > num:
            dec_seq.append(num)
        else:
            return "NO"

    inc_len = len(inc_seq)
    dec_len = len(dec_seq)

    print("YES")
    print(inc_len)
    print(*inc_seq)
    print(dec_len)
    print(*dec_seq[::-1])

# Reading input
n = int(input())
a = list(map(int, input().split()))

# Calling the function
split_sequence(n, a)
