
def calculate_bribe_articles(articles, impact_factor):
    total_citations = articles * impact_factor
    current_citations = 0
    scientists_to_bribe = 0
    
    while current_citations < total_citations:
        current_citations += articles
        scientists_to_bribe += 1
    
    return scientists_to_bribe

# Input
articles, impact_factor = map(int, input().split())

# Output
print(calculate_bribe_articles(articles, impact_factor))
