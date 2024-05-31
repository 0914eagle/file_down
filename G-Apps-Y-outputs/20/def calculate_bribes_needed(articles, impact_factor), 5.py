
def calculate_bribes_needed(articles, impact_factor):
    total_citations_needed = articles * impact_factor
    
    current_citations = 0
    scientists_bribed = 0
    
    while current_citations < total_citations_needed:
        current_citations += articles
        scientists_bribed += 1
    
    return scientists_bribed

# Read input
articles, impact_factor = map(int, input().split())

# Calculate and print the result
print(calculate_bribes_needed(articles, impact_factor))
