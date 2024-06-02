
 def max_element(l: list):
    
    if len(l) == 0:
        return None
    max_elem = l[0]
    for i in range(1, len(l)):
        if l[i] > max_elem:
            max_elem = l[i]
    return max_elem
 