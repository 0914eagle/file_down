
def fruit_distribution(s, n):
    # Split the input string to get the counts of apples and oranges
    counts = s.split()
    
    # Retrieve the counts of apples and oranges
    apples = int(counts[0]) if counts[0].isdigit() else 0
    oranges = int(counts[-1]) if counts[-1].isdigit() else 0
    
    # Calculate the number of mango fruits in the basket
    mango = n - apples - oranges
    
    return mango
