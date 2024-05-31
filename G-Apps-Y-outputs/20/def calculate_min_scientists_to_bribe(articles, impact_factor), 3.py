
def calculate_min_scientists_to_bribe(articles, impact_factor):
    total_citations_needed = articles * (impact_factor - 1)
    return total_citations_needed

# Input
articles, impact_factor = map(int, input().split())

# Output
print(calculate_min_scientists_to_bribe(articles, impact_factor))
