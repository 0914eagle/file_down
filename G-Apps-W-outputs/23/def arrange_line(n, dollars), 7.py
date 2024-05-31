
def arrange_line(n, dollars):
    dollars_sorted = sorted([(dollar, i) for i, dollar in enumerate(dollars, start=1)])
    
    result = [0] * n
    current_dollars = 1
    
    for dollar, position in dollars_sorted:
        if dollar < current_dollars:
            print(':(')
            return
        
        result[position-1] = current_dollars
        current_dollars += 1
    
    print(' '.join(map(str, result)))


# Input parsing
n = int(input())
dollars = list(map(int, input().split()))

# Function call
arrange_line(n, dollars)
