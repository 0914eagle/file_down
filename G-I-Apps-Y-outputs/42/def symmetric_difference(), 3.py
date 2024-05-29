
def symmetric_difference():
    # Input processing
    m = int(input())
    set_m = set(map(int, input().split()))
    
    n = int(input())
    set_n = set(map(int, input().split()))
    
    # Find symmetric difference and sort in ascending order
    result = sorted(set_m.symmetric_difference(set_n))
    
    # Output the result
    for val in result:
        print(val)

# Calling the function to find and print the symmetric difference
symmetric_difference()
