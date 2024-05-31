
def calculate_bribes(articles, impact_factor):
    total_citations = articles * impact_factor
    total_articles = articles
    total_bribes = max(0, total_citations - total_articles)
    return total_bribes

# Input
articles, impact_factor = map(int, input().split())

# Output
print(calculate_bribes(articles, impact_factor))
