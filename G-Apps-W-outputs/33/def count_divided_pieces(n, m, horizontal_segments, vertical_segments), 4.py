
def count_divided_pieces(n, m, horizontal_segments, vertical_segments):
    # Initialize the count of pieces to 1 (the original square)
    count = 1
    
    # Store the endpoints of all segments
    endpoints = []
    
    # Add horizontal segment endpoints
    for y, lx, rx in horizontal_segments:
        endpoints.append((y, lx, 0))  # 0 represents the start of the segment
        endpoints.append((y, rx, 1))  # 1 represents the end of the segment
        
    # Add vertical segment endpoints
    for x, ly, ry in vertical_segments:
        endpoints.append((ly, x, 0))  # 0 represents the start of the segment
        endpoints.append((ry, x, 1))  # 1 represents the end of the segment
    
    # Sort all endpoints based on y-coordinate, breaking ties with event type (0=start, 1=end)
    endpoints.sort()
    
    # Initialize a counter for active segments
    active_segments = 0
    
    # Iterate through sorted endpoints
    for i in range(len(endpoints)):
        y, x, event = endpoints[i]
        
        if event == 0:  # Start of a segment
            active_segments += 1
        else:  # End of a segment
            active_segments -= 1
        
        # If there are more than one active segments, it means a new piece is formed
        if active_segments > 1:
            count += 1
    
    return count

# Read input
n, m = map(int, input().split())
horizontal_segments = [list(map(int, input().split())) for _ in range(n)]
vertical_segments = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print the result
print(count_divided_pieces(n, m, horizontal_segments, vertical_segments))
