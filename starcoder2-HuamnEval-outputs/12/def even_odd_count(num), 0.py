
 def even_odd_count(num):
    num = str(num)
    even = 0
    odd = 0
    for i in num:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
 