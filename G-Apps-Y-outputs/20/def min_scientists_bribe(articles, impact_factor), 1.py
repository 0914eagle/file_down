
def min_scientists_bribe(articles, impact_factor):
    total_citations_needed = articles * impact_factor
    total_citations_current = 0
    
    for i in range(1, 1001):  # Assume maximum of 1000 scientists can be bribed
        total_citations_current = articles * ((total_citations_current + i) / articles)
        
        if total_citations_current >= total_citations_needed:
            return i

# Input handling
input_values = input().split()
articles = int(input_values[0])
impact_factor = int(input_values[1])

min_scientists = min_scientists_bribe(articles, impact_factor)
print(min_scientists)
