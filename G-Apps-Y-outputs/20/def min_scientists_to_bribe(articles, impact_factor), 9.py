
def min_scientists_to_bribe(articles, impact_factor):
    total_citations_needed = articles * impact_factor
    total_articles = articles

    scientists_to_bribe = total_citations_needed - total_articles
    return scientists_to_bribe

# Read input
articles, impact_factor = map(int, input().split())

# Calculate and print the minimal number of scientists needed to bribe
print(min_scientists_to_bribe(articles, impact_factor))
