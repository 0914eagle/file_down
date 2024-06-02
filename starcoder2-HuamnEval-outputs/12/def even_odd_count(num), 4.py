
 def even_odd_count(num):
    return (len(str(num)) - len(str(num).replace('0', '')), len(str(num)) - len(str(num).replace('1', '')))
 