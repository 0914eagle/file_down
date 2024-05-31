
def is_perfect_square(n):
    return n == int(n**0.5)**2

def shortest_subsequence_with_perfect_square_product(n, a):
    # Helper function to check if a product is a perfect square
    def has_perfect_square_product(products):
        for p in products:
            if is_perfect_square(p):
                return True
        return False
    
    # Initialize variables
    min_length = float('inf')
    products = []
    
    # Iterate through all subsequences
    for i in range(1, 2**n):
        subseq = []
        for j in range(n):
            if (i >> j) & 1:
                subseq.append(a[j])
        
        # Calculate product of subsequence
        product = 1
        for num in subseq:
            product *= num
        
        products.append(product)
        
        # Check if product is a perfect square
        if has_perfect_square_product(products):
            min_length = min(min_length, len(subseq))
    
    # Return result
    return min_length if min_length != float('inf') else -1

# Read input
n = int(input())
a = list(map(int, input().split()))

# Call the function and print the result
print(shortest_subsequence_with_perfect_square_product(n, a))
