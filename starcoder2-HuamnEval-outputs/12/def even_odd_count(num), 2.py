
 def even_odd_count(num):
    even = 0
    odd = 0
    num = abs(num)
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return (even, odd)
 