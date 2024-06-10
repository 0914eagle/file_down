
def calculate_time(h, m):
    m = m - 45
    if m < 0:
        m = m + 60
        h = h - 1
    
    if h < 0:
        h = h + 24
    
    return (h, m)

h, m = map(int, input().split())
h, m = calculate_time(h, m)
print(h, m)

