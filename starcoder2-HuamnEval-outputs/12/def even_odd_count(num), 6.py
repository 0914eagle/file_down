
def even_odd_count(num):
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

print(even_odd_count(-12))
print(even_odd_count(123))
print(even_odd_count(123456789))
 