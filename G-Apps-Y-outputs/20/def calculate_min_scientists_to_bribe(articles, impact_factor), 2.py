
def calculate_min_scientists_to_bribe(articles, impact_factor):
    total_citations_needed = articles * impact_factor
    total_citations_current = 0
    scientists_to_bribe = 0
    
    while total_citations_current < total_citations_needed:
        scientists_to_bribe += 1
        total_citations_current = total_citations_current + articles
        current_impact_factor = total_citations_current / articles
        
        if current_impact_factor > impact_factor:
            break
    
    return scientists_to_bribe

# Input processing
articles, impact_factor = map(int, input().split())

# Call the function and print the result
print(calculate_min_scientists_to_bribe(articles, impact_factor))
