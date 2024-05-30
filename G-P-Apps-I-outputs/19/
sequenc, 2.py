
sequence = input()

count_h = sequence.count('H')
count_t = sequence.count('T')
count_q = sequence.count('?')

if count_q == 0:
    average_ops = count_h + count_t
elif count_h + count_t == 0:
    average_ops = 0
else:
    average_ops = (count_h + count_t + count_q) / 2

print(average_ops)
```
