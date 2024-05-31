
def min_scientists_to_bribe(articles, impact_factor):
    total_citations = articles * impact_factor
    total_articles = articles
    while total_citations / total_articles > impact_factor:
        total_articles += 1
    return total_articles - articles

# Read input
articles, impact_factor = map(int, input().split())

# Calculate and output result
result = min_scientists_to_bribe(articles, impact_factor)
print(result)
