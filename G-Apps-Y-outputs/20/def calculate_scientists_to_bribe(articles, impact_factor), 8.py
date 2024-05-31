
def calculate_scientists_to_bribe(articles, impact_factor):
    total_citations_needed = articles * impact_factor
    total_citations_current = 0
    scientists = 0

    while total_citations_current < total_citations_needed:
        total_citations_current += articles
        scientists += 1

    return scientists

# Read input
articles, impact_factor = map(int, input().split())

# Calculate and output result
print(calculate_scientists_to_bribe(articles, impact_factor))
